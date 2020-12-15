name = "bill"
fname = f"{name}"
print(f"Hello, {fname}")

print(fname.upper())
print(fname.lower())
print(fname.title())

author = "Oscar Wilde"  
quote = '"Always forgive your enemies; nothing annoys them so much."'
fauthor = f"{author}"
fquote = f"{quote}"

print(f"{fauthor} once said, {fquote}")

message = f"{fauthor} once said, {fquote}"

print(message)

name_two = " Space "
fname_two = f"{name_two}"
print(f"\t{fname_two}")
print(f"\n{fname_two}")
print(fname_two)
print(fname_two.rstrip())
print(fname_two.lstrip())
print(fname_two.strip()) 
