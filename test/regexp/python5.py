r'foo#not a comment'
r'''
    (?x)        # multi-line regexp
        foo     # comment
'''
R'''
    (?x)        # not a
        foo     # comment
'''



r             : source.python, storage.type.string.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.single.python
foo#not a comment : source.python, string.regexp.quoted.single.python
'             : punctuation.definition.string.end.python, source.python, string.regexp.quoted.single.python
r             : source.python, storage.type.string.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.begin.python, source.python, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
(?x)          : source.python, storage.modifier.flag.regexp, string.regexp.quoted.triple.python
              : source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 multi-line regexp : comment.line.number-sign.python, source.python, string.regexp.quoted.triple.python
        foo      : source.python, string.regexp.quoted.triple.python
#             : comment.line.number-sign.python, punctuation.definition.comment.python, source.python, string.regexp.quoted.triple.python
 comment      : comment.line.number-sign.python, source.python, string.regexp.quoted.triple.python
'''           : punctuation.definition.string.end.python, source.python, string.regexp.quoted.triple.python
R             : source.python, storage.type.string.python, string.quoted.single.multi.raw.python
'''           : punctuation.definition.string.begin.python, source.python, string.quoted.single.multi.raw.python
    (?x)        # not a : source.python, string.quoted.single.multi.raw.python
        foo     # comment : source.python, string.quoted.single.multi.raw.python
'''           : punctuation.definition.string.end.python, source.python, string.quoted.single.multi.raw.python
