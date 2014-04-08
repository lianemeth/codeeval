package main

import "fmt"
import "log"
import "bufio"
import "os"
import "strings"
import "strconv"

type LinkedList struct{
	start *LinkedElement
	end *LinkedElement
}

type LinkedElement struct{
	next *LinkedElement
	item int
}

func NewLinkedList() *LinkedList{
	list := new(LinkedList)
	list.start = nil
	list.end = nil
	return list
}

func (list *LinkedList) Add(item int){
	node := new(LinkedElement)
	node.item = item
	if list.start != nil{
		aux := list.end
		aux.next = node
		node.next = nil
		list.end = node
	} else{
		list.start = node
		list.end = node
	}
}

func floyd(line []string) (int, int){
	if len(line) <= 1{
		return len(line), 0
	}
	linkedlist := NewLinkedList()
	for _, item := range line{
		n, _ := strconv.Atoi(item)
		linkedlist.Add(n)
	}
	tortoise := linkedlist.start
	hare :=  tortoise.next
	for tortoise != nil && hare != nil && tortoise.item != hare.item{
		tortoise = tortoise.next
		if hare.next != nil{
			hare = hare.next.next
		}
	}
	mu := 0
	tortoise = linkedlist.start
	if hare == nil{
		hare = tortoise.next
	}
	for tortoise!= nil && hare != nil && tortoise.item != hare.item{
		tortoise = tortoise.next
		if hare.next != nil{
			hare = hare.next
		}
		mu ++
	}
	lambda := 1
	hare = tortoise.next
	for hare != nil && tortoise.item != hare.item{
		hare = hare.next
		lambda ++
	}
	return lambda, mu
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		lam, mu := floyd(line)
		fmt.Println(strings.Join(line[mu:mu+lam]," "))
	}
}
