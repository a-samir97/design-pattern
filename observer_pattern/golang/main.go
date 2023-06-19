package main

func main() {
	IphoneItem := newItem("Iphone 15")

	observerOne := &Customer{id: "Observer One"}
	observerTwo := &Customer{id: "Observer Two"}

	IphoneItem.register(observerOne)
	IphoneItem.register(observerTwo)

	IphoneItem.updateAvailability()
}
