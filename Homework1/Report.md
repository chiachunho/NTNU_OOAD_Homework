# OOAD Homework1
## Team Memeber
+ 台科 B10615013 李聿鎧
+ 台科 B10615024 李韋宗
+ 台科 B10615026 温承勲
+ 台科 M10915109 何嘉峻


## Contents
### 1. Provide definitions for the following terms. How does each of the terms apply to OO notion of classes? Provide examples of both good and bad uses of the terms in a design of a class or a set of classes.
#### (a) Abstraction (抽象)

+ **Definition**
    
    + 某個實體能完成任務或解決問題的概念。讓系統的操作可以用簡單地概念 (Method name) 表示, 讓使用者可以不需要瞭解每個動作是如何實作的 (Hide Implementation)。
+ **Example**
    + 以 C++ 實作圖書館類別為例，只要呼叫 `rent_book()`、`return_book()`、`search_book()`即可執行借書、還書和查書的功能，不需要知道內部實作細節。
    + **優點:** 整合可以不需要在意實作細節。
    + **缺點:** 除錯可能因為不知道實作細節變困難。
    ```cpp
    class Library
    {
        public:
            void rent_book();
            void return_book();
            void search_book();
    }

    void Library::rent_book()
    {
        // Rent book
    }    
    void Library::return_book()
    {
        // Return book
    }
    void Library::search_book()
    {
        // Search book
    }
    ```

#### (b) Encapsulation (封裝)
+ **Definition:** 通常指資料隱藏，將不應該將物件內部暴露給外部世界的資料給隱藏起來。但封裝也能看作任何形式的隱藏 (類型、實作和設計等等)。
+ **Example:**
    + 以 C++ 實作師生系統為例，在 `Student` 中，我們將學生名稱 `name` 隱藏起來避免暴露給外部世界。另外，講師不會知道哪些是大學生 (Undergraduate)，哪些是研究生 (MastersStudent)，也就是說我們封裝了學生 (`Student`) 的類型。
    + **優點:** 不讓資料過度曝光，以免增添在不知情的情況下，內容被修改。
    + **缺點:** 資料只能間接存取，可能會造成效能的低落，還有找尋資料的存取的 Code Trace 變得複雜。
    ```cpp
    class Student
    {
        public:
            Student(string n):name(n) {}
            virtual void get_class(){}
            void get_name() { cout << "My name is " << this->name << endl; }
        private:
            string name;
    };
    class Undergraduate : public Student
    {
        public:
            using Student::Student;
            virtual void get_class() 
            { 
                this->get_name();
                cout << "I'm Undergraduate Student\n";
            }
    };
    class MastersStudent : public Student
    {
        public:
            using Student::Student;
            virtual void get_class()
            {
                this->get_name();
                cout << "I'm Masters Student\n";
            }
    };
    ```
    ```cpp
    int main()
    {
        vector<Student*> std_list;
        std_list.push_back(new Undergraduate("Bob"));
        std_list.push_back(new MastersStudent("Keven"));
        std_list.push_back(new Undergraduate("Any"));
        std_list.push_back(new MastersStudent("David"));
        return 0;
    };
    ```
    

#### \(c\) Cohesion (內聚)
+ **Definition:** 一個副程式內部組成部分之間相互關聯的緊密程度。
    
    + 把執行某個功能所需用到的程式與資料都集和在某一個模組（function, class, package, etc）之中，該模組可被視為一個單獨的個體執行。希望一個模組只做一件事情。
+ **Example:**
    + 以 C++ 實作員工基本資料系統，該Class只負責儲存單一員工的薪資、ID、電子郵件地址，一半的功能為設定初始值，另一半為取值，所有執行的功能都在單一Class中完成，因此達到Cohesion。
    + **優點:** 相關的資料可以容易找取，不會分散在太多地方。如果以計算機架構來說，也可以增加快取的 Space Locality。
    + **缺點:** 功能單調，不能做太多事情。

    ```cpp
    class Staff
    {
        public:
            set_salary(int sal) { salary = sal; }
            set_id(int id) { staff_id = id; }
            set_email(string email) { email_address = email; }
            int get_salary(){ return salary; }
            int get_id(){ return staff_id; }
            string get_email() { return email_address; }
        private:
            int salary;
            int staff_id;
            string email_address;
    }
    ```

#### (d) Coupling (耦合)
+ **Definition:** 一個副程式與其他副程式之間關聯的緊密程度。
    
    + 執行某功能時需要數個有關聯的模組，也就是說模組與模組之間有依賴關係。
+ **Example:**
    + 以 C++ 實作師生系統，其中每位學生有屬於自己的 ID 與 Grade，每位老師底下有屬於自己的學生，當老師要查詢學生的 ID 與 Grade 時會呼叫到 Student 的`get_id()`、`get_grade()`，因此兩個不同的 Class 產生耦合關係
    + **優點:** 可以提供很多的功能。
    + **缺點:** 不相關的資料的交互作用可能會很複雜,不易除錯,快取無法得到 Locality 的好處。

    ```cpp
    class Student
    {
        public:
            int get_id(){ return std_id; }
            int get_grade(){ return grade; }
            Student(int id, int g):std_id(id), grade(g){}
        private:
            int std_id;
            int grade;
    }

    class Teacher
    {
        public:
            void add_std(Student t) { stds.push_back(t); };
            int get_sid(Student t) 
            { 
                vector<Student>::iterator it = find (stds.begin(), stds.end(), t);
                if(it != stds.end()) return t.get_id(); 
            }
            int get_sgrade(Student t)
            {
                vector<Student>::iterator it = find (stds.begin(), stds.end(), t);
                if(it != stds.end()) return t.get_grade();
            }
        private:
            vector<Student>stds;
    }
    ```

### 2. Write a simple OO program that implements the Shape example in slide 5 of Chapter 1 but using an OO approach rather than the presented functional decomposition solution.

+ **程式語言:** Python 3.7
+ **如何執行**
    ```
    $ python main.py
    ```