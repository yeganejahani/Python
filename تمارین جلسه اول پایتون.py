while True:   
    print("""
)1( ثبت نمرات دانش‌آموزان در فایل
)2( شمارش تعداد خطوط فایل
)3( پیدا کردن دانش‌آموز برتر
)4( خروج""")
    choice = input("گزینه موردنظر را انتخاب کنید: ")

#(4)
    if choice == "4":
        print("برنامه بسته شد")
        break

#(1)
    elif choice == "1":
        with open("score.txt","w+") as scores:
            for s in range(3):
                name = input("نام دانش‌آموز: ")
                score = int(input("نمره: "))
                scores.write(name + "-" + str(score) + "\n")
                print("ثبت شد")
                scores.seek(0)
                for i in scores:
                    print(i)

#(2)
    elif choice == "2":
        with open("books.txt","w+") as book:
            book.write("شازده کوچولو \nبینوایان \nکیمیاگر \nقلعه حیوانات")
            book.seek(0)
            print("تعداد کتاب‌ها: ", len(book.readlines()))

#(3)
    elif choice == "3":
        with open("score.txt","r") as f:
            scores = f.readlines()
        max_name = ""
        max_score = 0
        sum_score = 0
        for i in scores:
            x = i.split("-")
            score = int(x[1])
            sum_score += score
            if score > max_score:
                max_score = score
                max_name = x[0]
        print("دانش‌آموز برتر: ", max_name)
        print("نمره: ", max_score)
        print("معدل کلاس: ", sum_score/len(scores))
        
        
    else:
        print("نامعتبر")