package main

type Cache struct {
	storage      map[string]string
	evictionAlgo EvicationAlgo
	capacity     int
	maxCapacity  int
}

func initCache(e EvicationAlgo) *Cache {
	storage := make(map[string]string)
	return &Cache{
		storage:      storage,
		evictionAlgo: e,
		capacity:     0,
		maxCapacity:  2,
	}
}

func (c *Cache) setEvicationAlgo(e EvicationAlgo) {
	c.evictionAlgo = e
}

func (c *Cache) add(key, value string) {
	if c.capacity == c.maxCapacity {
		c.evict()
	}
	c.capacity++
	c.storage[key] = value
}

func (c *Cache) get(key string) string {
	return c.storage[key]
}

func (c *Cache) evict() {
	c.evictionAlgo.evict(c)
	c.capacity--
}
