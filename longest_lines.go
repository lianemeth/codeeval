package main

import "fmt"
import "log"
import "sort"
import "bufio"
import "os"
import "strconv"

type ByLength []string

func (a ByLength) Len() int	{ return len(a) }
func (a ByLength) Swap(i, j int) { a[i], a[j] = a[j], a[i] }
func (a ByLength) Less(i, j int) bool { return len(a[i]) < len(a[j]) }

func nLongestLines (n int, lines []string){
	sort.Sort(ByLength(lines))
	for i:=len(lines)-1; i>len(lines)-n-1; i--{
		fmt.Println(lines[i])
	}
}

func main() {
    file, err := os.Open(os.Args[1])
    if err != nil {
        log.Fatal(err)
    }
    defer file.Close()
    scanner := bufio.NewScanner(file)
    scanner.Scan()
    n, _ := strconv.Atoi(scanner.Text())
    lines := make([]string, 1)
    for scanner.Scan() {
	    lines = append(lines, scanner.Text())
    }
    nLongestLines(n, lines)
}
