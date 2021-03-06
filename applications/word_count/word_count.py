def word_count(s):
    # Your code here
    cache = {}
    special_chars = '" : ; , . - + = / \ | [ ] { } ( ) * ^ &'.split()
    s2 = ''.join(c.lower() for c in s if not c in special_chars)
    for word in s2.split():
        cache[word] = cache[word] + 1 if word in cache else 1
    return cache


if __name__ == "__main__":
    print(word_count(""))
    print(word_count("Hello"))
    print(word_count('Hello, my cat. And my cat doesn\'t say "hello" back.'))
    print(word_count('This is a test of the emergency broadcast network. This is only a test.'))
