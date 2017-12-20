class RunLengthEncoder:

    def encode(self, input_string):
        print("Start: Encoding")
        # Demo 1
        if not input_string:
            return []

        count = 1
        prev = ''
        lst = []
        for character in input_string:
            if character != prev:
                if prev:
                    entry = (prev, count)
                    lst.append(entry)
                # Demo 2
                count = 1
                prev = character
            else:
                count += 1
        else:
            entry = (character, count)
            lst.append(entry)
        print(lst)
        return lst

    def decode(self, lst):
        print("Start: Decoding")
        q = ''
        for character, count in lst:
            q += character * count
        print(q)
        return q
