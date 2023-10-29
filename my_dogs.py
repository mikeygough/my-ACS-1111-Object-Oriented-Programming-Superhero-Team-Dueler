from dog import Dog

# instantiate
my_dog = Dog("Rex", "SuperDog")
print(my_dog)
print("name:", my_dog.name)
print("breed:", my_dog.breed)
my_dog.bark()

# instantiate another dog
my_other_dog = Dog("Annie", "SuperDog")
print(my_other_dog.name)

foo = Dog("Foo", breed="Corgi")
bar = Dog("Bar", breed="German Shephard")
baz = Dog("Baz", breed="Retriever")

foo.sit()
bar.roll_over()
bar.bark()
baz.sit()