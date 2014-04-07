package main

import "fmt"
import "bufio"
import "os"
import "log"
import "strconv"

var Fibos []int

func fibonacci(n int) int{
	var element int;
	if len(Fibos) > n{
		return Fibos[n]
	}
	for i := len(Fibos)-1; i < n; i++{
		element = Fibos[i] + Fibos[i-1]
		Fibos = append(Fibos, element)
	}
	return element
}

func main() {
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var n int
	Fibos = append(Fibos, 0, 1)
	for scanner.Scan(){
		n, _ = strconv.Atoi(scanner.Text())
		fmt.Println(fibonacci(n))
	}
}

