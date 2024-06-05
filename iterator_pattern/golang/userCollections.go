package main

type UserCollection struct {
	users []*User
}

func (u *UserCollection) createIterator() Iterator {
	return &UserCollection{
		users: u.users,
	}
}
