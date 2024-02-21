class Contact:
    """
    Attributes: 
      fn (str) : first_name
      ln (str) : last_name
      pn (str) : phone_number
      addr (str) : address
      city (str) : city
      zip_code (int) : zipcode
    """

    def __init__(self, fn, ln, pn, addr, city, zip_code):
        self.fn = fn
        self.ln = ln
        self.pn = pn
        self.addr = addr
        self.city = city
        self.zip_code = zip_code

    def __lt__(self, other):
        if self.ln == other.ln:
            return self.fn < other.fn
        else:
            return self.ln < other.ln

    def __str__(self):
        return f"{self.fn}, {self.ln}\n{self.pn}\n{self.addr}\n{self.city}, {self.zip_code}\n"

    def __repr__(self):
        return f"{self.fn},{self.ln},{self.pn},{self.addr},{self.city},{self.zip_code}\n"
