from pydantic import BaseModel ,EmailStr


class simple_class(BaseModel):
    name :str
    age :int
    # email :EmailStr


dat = simple_class(name ="tarak",age =89  )
print(dat)
