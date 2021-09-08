def check(string):
    crt = {'open': 1}
    count = 0
    for i in string:
        # 0 სწორია შეცვლილი ან დაამატე 0
        if i == "(":
            # თუ ღიაა სწორია
            if crt['open'] == 0:
                return 'არასწორია'

            # გახსნა
            else:
                crt["open"] = 0

        # 1 არასწორია ან 0 იანია და დახურე
        elif i == ")":
            # თუ ღია არაა არასწორია
            if crt["open"] != 0:
                return "არასწორია"
            # დახურვა
            else:
                crt["open"] = 1

    if crt['open'] == 0:
        return 'არასწორია'

    elif crt['open'] == 1:
        return "სწორია"

print(check(""))
