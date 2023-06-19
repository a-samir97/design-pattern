package main 

type EvicationAlgo interface {
	evict (c *Cache)
}
