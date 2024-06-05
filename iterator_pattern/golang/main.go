package main

import "fmt"

func main() {
	user1 := &User{
		name: "Ahmed Samir",
		age:  12,
	}

	user2 := &User{
		name: "Nanna",
		age:  22,
	}

	userCollection := &UserCollection{
		users: []*User{user1, user2},
	}

	iterator := userCollection.createIterator()

	for iterator.hasNext() {
		user := iterator.getNext()

		fmt.Println(user)
	}
}
