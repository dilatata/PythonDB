import cx_Oracle

def dept01_create():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        cur = conn.cursor()
        try:
            cur.execute('drop table dept01')
        except Exception as e:
            print(e)
            cur.execute('create table dept01 as select * from dept')
            cur.execute('alter table dept01 add constraint dept01_uk_deptno unique(deptno)')
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def dept01_query(find_dname):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("select * from dept01 where dname like :dname", dname=find_dname)
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def dept01_query2():
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("select * from dept01")
            rows = cur.fetchall()
            for row in rows:
                print(row)
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()
        

def dept01_insert(new_deptno, new_dname, new_loc):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("insert into dept01 values(:deptno, :dname, :loc)", deptno=new_deptno, dname=new_dname, loc=new_loc)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()



def dept01_update(deptno, new_dname, new_loc):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("update dept01 set dname=:dname, loc=:loc where deptno=:deptno", dname=new_dname, loc=new_loc, deptno=deptno)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def dept01_update2(deptno, new_loc):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("update dept01 set loc=:loc where deptno=:deptno", loc=new_loc, deptno=deptno)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


def dept01_delete(deptno):
    try:
        conn = cx_Oracle.connect(user="SCOTT", password="TIGER", dsn="xe")
        try:
            cur = conn.cursor()
            cur.execute("delete from dept01 where deptno=:deptno", deptno=deptno)
            conn.commit()
        except Exception as e:
            print(e)
        finally:
            cur.close()
    except Exception as e:
        print(e)
    finally:
        conn.close()


if __name__ == '__main__':
    # dept01_create()

    dept01_insert(50, 'PD', '??????')
    # dept01_query2()
    # dept01_query('%ING')

    dept01_update(50, 'Playdata','??????')
    # dept01_query2()

    dept01_update2(50, '??????')
    dept01_query2()

    # dept01_delete(50)
    # dept01_query('%ING')

    # dept01_query()
