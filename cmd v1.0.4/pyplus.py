def compile(code: str) -> None:
    tokens = {};
    noWhitespaceCode: str;
    for i, v in enumerate(code):
        if(v == "\n"): continue;
        comment = v.find("//");
        if(comment == 0): continue;
        if(comment != -1):
            v = v[0:comment];
        noWhitespaceCode.append(v.replace("\n",""));
    print(noWhitespaceCode);
