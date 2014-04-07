package main

import "fmt"
import "log"
import "bufio"
import "strconv"
import "os"

func convertBin(n int) string{
	var out string
	for n > 0{
		out = out + strconv.Itoa(n % 2)
		n = n / 2
	}
	return out
}

func countOne(b string) int{
	sum := 0
	for i:=0; i<len(b); i++{
		if b[i] == '1'{
			sum ++
		}
	}
	return sum
}

func main(){
	var bin string
	file, err := os.Open(os.Args[1])
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		n, _ := strconv.Atoi(scanner.Text())
		bin = convertBin(n)
		fmt.Println(countOne(bin))
	}
}
