package manager

import (
	"bufio"
	"errors"
	"io"
	"log"
	"os"
	"sync"
	"time"
)

type Publisher struct {
	Locker            sync.Mutex
	Subscribers       map[string]chan string
	SubscribersErrors map[string]chan error
	Filepath          string // a file from where it reads and publishes data to all subscribers. change publisher source as required.
}

type Subscriber struct {
	Id string
	// add any required subscriber field here
}

func (p *Publisher) Send(data string) {

	p.Locker.Lock()
	defer p.Locker.Unlock()

	defer func() {
		if r := recover(); r != nil {
			log.Println("Sending data got error")
		}
	}()

	for _, v := range p.Subscribers {
		v <- data
	}

}

func (p *Publisher) StartPublisher() {
	// publish any required message here
	// for now i will just read a file and publish each and everyline continously

	time.Sleep(time.Second * 5)
	// just making sure that  publisher doesn't start publishing before subscriber subscribe
	file, err := os.Open(p.Filepath)
	if err != nil {
		log.Fatal("Unable to open publisher file")
	}
	defer file.Close()
	fileReader := bufio.NewReader(file)

	for {
		content, err := fileReader.ReadBytes('\n')
		if err == io.EOF {
			log.Println("reached end.")
			break
		}

		p.Send(string(content))

	}

}

func (p *Publisher) StartSubscriber(subscriber Subscriber) {
	// maintain atomicity in this part of code
	p.Locker.Lock()
	ch := make(chan string)
	errCh := make(chan error)
	p.Subscribers[subscriber.Id] = ch
	p.SubscribersErrors[subscriber.Id] = errCh
	p.Locker.Unlock()
	log.Printf("Subscriber %v initalized successfully", subscriber.Id)
	defer func() {
		// should HARDLY ever panic. Almost never panics just for unforeseen circumstances.
		if err := recover(); err != nil {
			log.Printf("Subscriber %v teminated cause of panic", subscriber.Id)
			p.SafeRemove(subscriber.Id)

		}

		close(ch)
		close(errCh)
	}()

	// subscriber will listen forever as long as it receives message on err channel
	for {
		select {
		case value := <-ch:
			log.Printf("Received value %v on subscriber %v", value, subscriber.Id)

		case <-time.After(time.Second * 30):
			log.Printf("Haven't received log in 30 sec on subsccriber %v", subscriber.Id)

			select {
			case <-errCh:
				log.Printf("Detected error on subscriber %v", subscriber.Id)
				return
			default:
				continue
			}

		}
	}

}

func (p *Publisher) RemoveSubscriber(SubscriberId string) {
	p.Locker.Lock()
	defer p.Locker.Unlock()
	p.SubscribersErrors[SubscriberId] <- errors.New("parent request to kill")
	delete(p.Subscribers, SubscriberId)
	delete(p.SubscribersErrors, SubscriberId)

}

// Only if subscriber ever panics will this function be activated
func (p *Publisher) SafeRemove(SubscriberId string) {
	p.Locker.Lock()
	defer p.Locker.Unlock()
	delete(p.Subscribers, SubscriberId)
	delete(p.SubscribersErrors, SubscriberId)

}
