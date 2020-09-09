if __name__ == "__main__":
    items = ['mountains', 'rivers', 'countries', 'cities', 'languages', 'whatever']

    print(len(items))
    print(sorted(items))
    items.sort()
    print(items)
    del items[0]
    items.remove('rivers')
    print(items)
    item = items.pop()
    print(item)
    items.append('money')
    print(items)
