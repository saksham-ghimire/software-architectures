package main

// the or-channel concurrency pattern is to be implemented in scenario where receiving signal in any subsquent channel should terminate/effect entirety of other spawned channels
// implements fun non blocking approach
import (
	"fmt"
	"time"
)

// this function just implements read operation of channel
// to implement write operation of channel the function would look something like
// var or func(channels ...chan<- interface{}) <-chan interface{}

// The or channel will close if any of the components channel receive close signal
// This implements recursive function that structures channel into tree branch

var or func(channels ...<-chan interface{}) <-chan interface{}

func main() {
	or = func(channels ...<-chan interface{}) <-chan interface{} {
		switch len(channels) {
		case 0:
			return nil
		case 1:
			return channels[0]
		}
		orDone := make(chan interface{})
		go func() {
			defer close(orDone)
			switch len(channels) {
			case 2:
				select {
				case <-channels[0]:
				case <-channels[1]:
				}
			default:
				select {
				case <-channels[0]:
				case <-channels[1]:
				case <-channels[2]:
				// we are passing the orDone channel so when goroutine up the tree exits goroutine down the tree also exits automatically
				case <-or(append(channels[3:], orDone)...):
				}
			}
		}()
		return orDone
	}

	sig := func(after time.Duration) <-chan interface{} {
		c := make(chan interface{})
		go func() {
			defer close(c)
			time.Sleep(after)
		}()
		return c
	}
	start := time.Now()
	<-or(
		sig(2*time.Hour),
		sig(5*time.Minute),
		sig(1*time.Second),
		sig(1*time.Hour),
		sig(1*time.Minute),
	)
	fmt.Printf("done after %v", time.Since(start))

}
