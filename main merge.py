import mysql.connector as msq
con=msq.connect(host="localhost",
                user="root",passwd="bangtan7",
                database="project")
import pandas as pd

#logging in the cred table

tasks="n"
while tasks=="n":
    print("--A-for LOGIN")
    print("--B-for SIGNUP")
    print("--C-to EXIT")
    a6=input("enter task:").upper()
    if a6=="A":
        uname=input("enter username:")
        paswd=input("enter password:")
        cn=con.cursor(buffered=True)
        a="select user_n from cred where user_n=%s"
        cn.execute(a,(uname,))
        con.commit()
        row=cn.fetchone()
        if not row:
            print("username not found. try signing up first")
            continue
        else:
            for i in row:
                if i==uname:
                    print("successfully logged in!")
                    print("")
                    
                

        #department management functions
        dmng="n"
        while dmng=="n":
            print("--D-for employee functions")
            print("--E-for department functions")
            print("--F-for post functions")
            print("--G-to update or delete loginID and password")
            print("--H-to add/delete employee personal details")
            print("--I-to display employee personal detail")
            print("--J-to add/delete office details")
            print("--K-to display office details")
            print("--L-to add or update salary details")
            print("--M-to display salary details")
            print("--0-to logout")
            b6=input("enter task:").upper()
            if b6=="D":
                #employee details functions
                x="n"
                while x=="n":
                    print("""
                        --1-all staff details
                        --2-search employee by employee id
                        --3-change employee details
                        --4-add new employee
                        --5-delete employee details
                        --0-exit staff functions""")
                    b1=input("enter:")
                    #all details
                    if b1=="1":
                        cn=con.cursor(buffered=True)
                        cn.execute("select * from staff")
                        c=cn.fetchall()
                        if not c:
                            print("no employee names are in record. to add new employee names,click 4 ")
                        else:
                            for i in c:
                                print(i)
                                con.commit()
                                print("try another function")
                                            
                                    
                    #searching by id
                    if b1=="2":
                        y="y"
                        while y=="y":
                            eid=input("enter employee ID:").lower()
                            cn=con.cursor(buffered=True)
                            h="select * from staff where s_id=%s"
                            cn.execute(h,(eid,))
                            n=cn.fetchone()
                            if not n:
                                print("you entered invalid ID")
                            else:
                                cn=con.cursor(buffered=True)
                                fg="select * from staff where s_id=%s"
                                cn.execute(fg,(eid,))
                                con.commit()
                                for i in cn:
                                    print(i)
                            y=input("search another ID?(y/n):")
                        else:
                            print("invalid response, try other staff functions:")
                            print("")

                #changing emp details
                    if b1=="3":
                        y="y"
                        while y=="y":
                            cn=con.cursor()
                            eid=input("enter employee ID:")
                            j="select * from staff where s_id=%s"
                            cn.execute(j,(eid,))
                            xx=cn.fetchone()
                            if xx==None:
                                print("you entered invalid ID")
                                continue
                            else:
                                print("""
                                --1-change name
                                --2-change contact
                                --3-change address
                                --4-change salary""")
                                a2=input("enter:")
                                if a2=="1":
                                    a3=input("enter new name:")
                                    cn=con.cursor()
                                    k="update staff set s_name=%s where s_id=%s"
                                    cn.execute(k,(a3,eid))
                                    con.commit()
                                    print("name record updated successfully")
                                if a2=="2":
                                    a3=input("enter new valid contact(10 digit):")
                                    cn=con.cursor()
                                    l="update staff set s_phone=%s where s_id=%s"
                                    cn.execute(l,(a3,eid))
                                    con.commit()
                                    print("contact record updated successfully")
                                if a2=="3":
                                    a3=input("enter new address")
                                    cn=con.cursor()
                                    m="update staff set s_addr=%s where s_id=%s"
                                    cn.execute(m,(a3,eid))
                                    con.commit()
                                    print("adress record updated successfully")
                                if a2=="4":
                                    a3=input("enter new salary")
                                    cn=con.cursor()
                                    n="update staff set s_salary=%s where s_id=%s"
                                    cn.execute(n,(a3,eid))
                                    con.commit()
                                    print("salary record updated successfully")
                            y=input("change more details?(y/n):")
                            if y=="n":
                                print("try another function")
                                break
                            else:
                                continue

                            #adding new emp
                                
                    if b1=="4":
                        nid=input("enter ID:").lower()
                        nm=input("enter name:")
                        nad=input("enter address:")
                        nap=input("enter contact:")
                        nsa=input("enter salary:")
                        npo=input("enter post:")
                        cn=con.cursor()
                        cn.execute("select s_id from staff where s_id=%s",(nid,))
                        y=cn.fetchone()
                        if y==None and len(nap)==10:
                            nb="insert into staff(s_id,s_name,s_addr,s_phone,s_salary,s_post) values(%s,%s,%s,%s,%s,%s)"
                            cn.execute(nb,(nid,nm,nad,nap,nsa,npo))
                            con.commit()
                                        
                            print("details saved successfully")
                            print("try out other functions")
                        else:
                            print("ID already exists or invalid contact")                
                                    
                            #deleting emp details
                    if b1=="5":
                        ab=input("enter employee ID you want to delete:")
                        cn=con.cursor()
                        b="select * from staff where s_id=%s"
                        cn.execute(b,(ab,))
                        xy=cn.fetchone()
                        if xy==None:
                            print("invalid ID")
                        else:
                            hj="delete from staff where s_id=%s"
                            cn.execute(hj,(ab,))
                            con.commit()
                                        
                            print("ID record removed successfully")
                                    

                            #exiting staff functions
                    if b1=="0":
                        x="y"
                        print("staff functions closed")
                        print("")

                
            if b6=="E":
                #department functions
                x="n"
                while x=="n":
                    print("""
                        --1-to see all departments
                        --2-to search department
                        --3-to add department
                        --4-to remove department
                        --5-to update department
                        --0-to exit department functions""")
                    a3=input("enter:")
                    #see department
                    if a3=="1":
                        cn=con.cursor()
                        cn.execute("select * from department")
                        x=cn.fetchall()
                        if not x:
                            print("no departments available yet. create one yourself!")
                            print("")
                        else:
                            for i in x:
                                print(i)
                                print("")
                                con.commit()

                    #searching dept
                    if a3=="2":
                        ad="y"
                        while ad=="y" or ad=="Y" :
                            ac=input("enter department code:")
                            cn=con.cursor()
                            cn.execute("select * from department where deptcode=%s",(ac,))
                            xb=cn.fetchone()
                            if xb==None:
                                print("invalid code")
                            else:
                                cn.execute("select * from department where deptcode=%s",(ac,))
                                for i in cn:
                                    print(i)
                            ad=input("search other departments?(y/n):")
                    #adding dept
                    if a3=="3":
                        ad="y"
                        while ad=="y" or ad=="Y":
                            ic=input("enter new department code:")
                            ina=input("enter department name:")
                            ip=input("enter department package:")
                            cn=con.cursor()
                            cn.execute("select * from department where deptcode=%s",(ic,))
                            x=cn.fetchall()
                            if not x:
                                cn.execute("insert into department values(%s,%s,%s)",(ic,ina,ip))
                                con.commit()
                                print("new department added successfully")
                                
                            else:
                                print("department code already exists")
                            ad=input("enter more departments?(y/n):")
                                
                    #deleting dept
                    if a3=="4":
                        ad="y"
                        while ad=="y" or ad=="Y":
                            cn=con.cursor()
                            ax=input("enter department code:")
                            cn.execute("select * from department where deptcode=%s",(ax,))
                            xa=cn.fetchone()
                            if not xa:
                                print("invalid ID")
                            else:
                                cn.execute("delete from department where deptcode=%s",(ax,))
                                con.commit()
                                print("department deleted successfully")
                            ad=input("remove more departments?(y/n):")
                    #updating dept
                    if a3=="5":
                        ad="y"
                        while ad=="y" or ad=="Y":
                            print("""
                                    --N-to change department name
                                    --P-to change department package""")
                            i=input("enter:").upper()
                            if i=="N":
                                e="y"
                                while e=="y" or "Y":
                                    j=input("enter department code")
                                    nn=input("enter new department name")
                                    cn=con.cursor()
                                    bn="select * from department where deptcode=%s"
                                    cn.execute(bn,(j,))
                                    cx=cn.fetchone()
                                    if not cx:
                                        print("invalid code")
                                    else:
                                        add_produto="update department set deptname=%s where deptcode=%s"
                                        cn.execute(add_produto,(nn,j))
                                        con.commit()
                                        print("department name updated successfully")
                                    e=input("update more department names?(y/n):")
                            if i=="P":
                                e="y"
                                while e=="y" or e=="Y":
                                    j=input("enter department code")
                                    np=input("enter new package")
                                    cn=con.cursor()
                                    bm="select * from department where deptcode=%s"
                                    cn.execute(bm,(j,))
                                    cx=cn.fetchone()
                                    if cx==None:
                                        print("invalid code")
                                    else:
                                        add_produto="update department set deptpackage=%s where deptcode=%s"
                                        cn.execute(add_produto,(np,j))
                                        con.commit()
                                        print("department package record updated successfully")
                                    e=input("update other department packages?(y/n):")
                    #exiting dept functions
                    if a3=="0":
                        x="y"
                        print("department functions closed")

            
            if b6=="F":
                #post functions
                qp="n"
                while qp=="n":
                    print("""
                            --1-to see list of posts
                            --2-to update post
                            --3-to remove or add post
                            --0-to exit post functions""")
                    a4=input("enter:")

                    #viewing list of posts
                    if a4=="1":
                        cn=con.cursor(buffered=True)
                        cn.execute("select post_name from post")
                        d=cn.fetchall()
                        for i in d:
                            print(i)
                            con.commit()
                        print("")
                        print("try another function")
                    #updating post
                    if a4=="2":
                        r="y"
                        while r=="y" or r=="Y":
                            cn=con.cursor()
                            c=input("enter post code:")
                            cn.execute("select * from post where post_code=%s",(c,))
                            vx=cn.fetchone()
                            if vx==None:
                                print("invalid post code")
                            else:
                                uq=int(input("enter new total number of employee:"))
                                v="update post set no_of_employees=%s where post_code=%s"
                                cn.execute(v,(str(uq),c))
                                con.commit()
                                
                                print("number of employee updated successfully")
                            r=input("change more records?(y/n):")
                    #adding and deleting posts
                    if a4=="3":
                        ui="y"
                        while ui=="y" or ui=="Y":
                            print("""
                                  --i-to add new post
                                  --j-to remove post""")
                            rr=input("enter:").lower()
                            if rr=='i':
                                df="y"
                                while df=="y" or df=="Y":
                                    cn=con.cursor()
                                    it=input("enter post code:")
                                    itt=input("enter post name:")
                                    itp=input("enter no. of employee")
                                    cn.execute("select post_code from post where post_code=%s",(it,))
                                    xt=cn.fetchall()
                                    if not xt:
                                        lo="insert into post values(%s,%s,%s)"
                                        cn.execute(lo,(it,itt,itp))
                                        con.commit()
                                        print("new post added successfully")
                                    else:
                                        print("post code already exists")
                                    df=input("add more posts?(y/n)")
                                    if df=="n":
                                        ui=input("add or remove more records?(y/n)")
                                        
                            if rr=="j":
                                op="y"
                                while op=="y" or op=="Y":
                                    itc=input("enter post code")
                                    cn=con.cursor()
                                    cn.execute("select post_code from post where post_code=%s",(itc,))
                                    xz=cn.fetchone()
                                    if not xz:
                                        print("invalid post code")
                                    else:
                                        cn.execute("delete from post where post_code=%s",(itc,))
                                        con.commit()
                                        print("post removed successfully")
                                    op=input("delete more posts?(y/n):")
                    #exiting post functions
                    if a4=="0":
                        qp="y"
                        print("posts functions closed")

            if b6=="G":
                #login id & password functions
                lk="n"
                while lk=="n" or lk=="LK":
                    print("""
                            --a-for updating loginID or password
                            --b-for removing an ID
                            --x-for exiting the function""")
                    jkl=input("enter:").lower()
                    if jkl=="a":
                        ty="y"
                        while ty=="y" or ty=="Y":
                            print("""
                                    --1-to update loginID
                                    --2-to update password""")
                            rt=input("enter:")
                            if rt=="1":
                                nm="y"
                                while nm=="y" or nm=="Y":
                                    cn=con.cursor()
                                    oid=input("enter old loginID")
                                    nid=input("enter new loginID")
                                    cn.execute("select * from cred where user_n=%s",(oid,))
                                    xb=cn.fetchone()
                                    if xb==None:
                                        print("ID does not exist")
                                    else:
                                        vb="update cred set user_n=%s where user_n=%s"
                                        cn.execute(vb,(nid,oid))
                                        con.commit()
                                        
                                        print("loginID updated successfully")
                                    nm=input("update more loginID?(y/n):")

                            if rt=="2":
                                nm="y"
                                while nm=="y" or nm=="Y":
                                    cn=con.cursor()
                                    oid=input("enter loginID:")
                                    npd=input("enter new password:")
                                    cn.execute("select * from cred where user_n=%s",(oid,))
                                    xm=cn.fetchone()
                                    if xm==None:
                                        print("ID does not exist")
                                    else:
                                        j="update cred set passwd=%s where user_n=%s"
                                        cn.execute(j,(npd,oid))
                                        con.commit()
                                        
                                        print("password updated successfully")
                                    nm=input("update more passwords?(y/n):")
                            ty=input("change more loginID or passwords?(y/n):")
                    if jkl=="b":
                        nm="y"
                        while nm=="y" or nm=="Y":
                            cn=con.cursor()
                            oid=input("enter loginID")
                            cn.execute("select * from cred where user_n=%s",(oid,))
                            h=cn.fetchone()
                            if h==None:
                                print("ID does not exist")
                            else:
                                cn.execute("delete from cred where user_n=%s",(oid,))
                                con.commit()
                                print("loginID removed successfully")
                            nm=input("remove more id?(y/n)")
                    if jkl=="x":
                        lk="y"
                        print("login functions closed")


            if b6=="H":
                print("""--1-to add data
--2-to delete data""")
                zz=input("enter:")
                if zz=="1":
                    y="y"
                    while y=="y":
                        n=input("enter employee name:")
                        c=input("enter enployee's city name:")
                        d=input("enter employee's d.o.b(YYYY-MM-DD):")
                        p=input("enter employee's phone:")
                        g=input("enter employee's gender:")
                        data=(n,c,d,p,g) 
                        sql='insert into personal values(%s,%s,%s,%s,%s)'
                        cn=con.cursor()
                        cn.execute(sql,data)
                        con.commit()
                        print("data has been entered successfully")
                        y=input("add more personal details?(y/n):")
                elif zz=="2":
                    y="y"
                    while y=="y":
                        n=input("enter employee name:")
                        p=input("enter employee phone:")
                        sql="delete from personal where phone=%s"
                        cn=con.cursor()
                        cn.execute(sql,(p,))
                        con.commit()
                        print("data has been removed successfully")
                        y=input("remove more personal details?(y/n):")

            if b6=="I":
                sql="select name,city,dob,phone from personal"
                cn=con.cursor()
                cn.execute(sql)
                d=cn.fetchall()
                if not d:
                    print("no data availale")
                    print("")
                else:
                    print("")
                    print("displaying personal details in the format:")
                    headers = [i[0] for i in cn.description]
                    print(headers)
                    print("")
                    for i in d:
                        print(i)
                        print("")
            if b6=="J":
                zz=input("""--1-to add data
--2-to delete data""")
                if zz=="1":
                    y="y"
                    while y=="y":
                        ec=input("enter employee code:")
                        m=input("enter employee name:")
                        ps=input("enter emploee's post:")
                        j=input("enter employee's joining date(DD/MM/YYYY):")
                        bp=int(input("enter assigned basic pay:"))
                        data=(ec,n,ps,j,bp)
                        sql='insert into office values(%s,%s,%s,%s)'
                        cn=con.cursor()
                        cn.execute(sql,data)
                        con.commit()
                        print("data has been entered successfully")
                        y=input("add more employee?(y/n):")
                elif zz=="2":
                    while y=="y":
                        ec=input("enter employee code:")
                        sql='delete from office where ecode=%s'
                        cn=con.cursor()
                        cn.execute(sql,(ec,))
                        con.commit()
                        print("data has been removed successfully")
                        y=input("remove more employee?(y/n):")

                    
            if b6=="K":
                sql="select * from office"
                cn=con.cursor()
                cn.execute(sql)
                d=cn.fetchall()
                if not d:
                    print("no data available")
                    print("")
                else:
                    print("")
                    print("displaying office details in the format:")
                    headers = [i[0] for i in cn.description]
                    print(headers)
                    print("")
                    for i in d:
                        print(i)
                        print("")
            if b6=="L":
                y="y"
                while y=="y":
                    ec=input("enter employee code")
                    v=(ec,) 
                    sql="select basicpay from office where ecode=%s"
                    cn=con.cursor()
                    cn.execute(sql,v)
                    bs=cn.fetchone() #to fetch only one row
                    n=input("enter employee name:")
                    y=input("enter year(YYYY):")
                    m=input("enter month(in letters):")
                    wd=input("enter working days(in numbers):")
                    td=input("enter total days in the month(in numbers):")
                    fp=bs[0]/td*wd #final pay of the employee, 0 index would have salary like (30000,)
                    data=(ec,n,y,m,wd,fp)
                    sql='insert into salary values(%s,%s,%s,%s,%s,%s)'
                    cn=con.cursor()
                    c.execute(sql,data)
                    con.commit()
                    print("data has been entered successfully")
                    y=input("add/update more salary rows?(y/n):")
            

            if b6=="M":
                sql="select * from salary"
                cn=con.cursor()
                cn.execute(sql)
                d=cn.fetchall()
                if not d:
                    print("no data available")
                    print("")
                else:
                    print("")
                    print("displaying salary details in the format:")
                    headers = [i[0] for i in cn.description]
                    print(headers)
                    print("")
                    for i in d:
                        print(i)
                    print("")
            if b6=="0":
                print("logged out successfully")
                break

    if a6=="B":
    #signup functions
        y="y"
        while y=="y" or y=="Y":
            us=input("enter username:")
            up=input("enter password:")
            cn=con.cursor()
            cn.execute("select * from cred where user_n='"+us+"'")
            cc=cn.fetchone()
            if cc==None:
                cn.execute("insert into cred values('"+us+"','"+up+"')")
                con.commit()
                print("saved successfully")
            else:
                print("username/loginID already exists. Try logging in")
            y=input("create a new id?(y/n):")
        else:
            print("try out a different function")
            print("")
                                           
    #program closer/exiting
    if a6=="C":
       tasks="y"
       print("exited successfully, all functions closed")
       print("run the program again to restart. Thankyou!") 

                               
                        
                    




                    
                    
                        
            
                    

                                                
                    
        
        
