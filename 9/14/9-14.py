from die import Die

die = Die()
for index in range(1, 10):
    die.roll_die()

die = Die(10)
for index in range(1, 10):
    die.roll_die()

die = Die(20)
for index in range(1, 10):
    die.roll_die()
