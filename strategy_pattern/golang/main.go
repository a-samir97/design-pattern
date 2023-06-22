package main

func main() {
	lfu := &Lfu{}

	cache := initCache(lfu)

	cache.add("test_1", "123")
	cache.add("test_2", "456")
	cache.add("test_3", "789")

	lru := &Lru{}

	cache.setEvicationAlgo(lru)

	cache.add("test_44", "test")

	fifo := &Fifo{}

	cache.setEvicationAlgo(fifo)

	cache.add("Test_FIFO", "FIFO")

}
