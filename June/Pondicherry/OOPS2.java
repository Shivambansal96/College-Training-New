// // Polymorphism
// class Student {
//     String name;
//     int age;

//     // Method Overloading - CompileTime (Same MethodName but Different Parameters)
//     public void printInfo(String name) {
//         System.out.println(name);
//     }

//     public void printInfo(int age) {
//         System.out.println(age);
//     }

//     public void printInfo(String name, int age) {
//         System.out.println(name + " " + age);
//     }    
// }


// // Method Overriding RunTime  (Same MethodName AND Different Parameters)
// class Animal{

//     public void sound() {
//         System.out.println("Animal makes a sound.");
//     }
// }

// class Dog extends Animal {
//     @Override
//     public void sound() {
//         System.out.println("Dog Barks.");
//     }
// }

// class Cat extends Animal {
//     @Override
//     public void sound() {
//         System.out.println("Cat Meows.");
//     }
// }



// // // Inheritance

// class Shape {
//     String color;

//     public void area() {
//         // System.out.println("");
//     }
// }


// class  Animal {
    
// }

// class Triangle extends Shape {

//     public void area(int l, int h) {
//         System.out.println(2* l * h);
//     }

// }

// class Equilateral extends Triangle {
    
//     public void area(int h, int l, int b) {
//         if( l+ b + h == 180)
//         System.out.println("Equilateral Triangle");
//         else
//         System.out.println("Not Equilateral Triangle");
        
        
//     }
// }

// // Access Modifier

// class Student {
//     String name;
//     private String email;
//     protected String emailvw;

//     // getter & setter
//     public String getPassword(String email) {
//         this.email = setPassword("name");
//         return email;
//     }

//     private String setPassword(String pass) {
//         this.email = pass;
//     }

// }



// // // Abstraction
// abstract class Animal {
//     abstract void walk();

//     public void eat() {
//         System.out.println("Some animals donot eat.");
//     }


// }

// class Cats extends Animal {

//     public void walk() {
//         System.out.println(".()");
//     }

//     public void eat() {
//         System.out.println("Fish");

//     }
// }

// class Horse extends Animal {

//     public void walk() {
//         System.out.println("Can walk on 4 legs.");
//     }
// }

// class Kangaroo extends Animal {
//     public void walk() {
//         System.out.println("Can walk on 2 legs.");
//     }
// }


// interface Animal {
//     String name = "Dog";

//     public void sound();
// }

// interface Plants {
//     String name = "Plant";

//     public void eat();
// }


// class Dog implements Animal, Plants {
//     public void sound() {
//         System.out.println(".()");
//     }
//     public void eat() {
//         System.out.println(".()");
//     }
// }


class Student {
    String name;
    int age;
    static String clgName;


    public void printInfo() {
        System.out.println(this.name);
        System.out.println(this.age);
        System.out.println(this.clgName);
    }
}


public class OOPS2 {
    public static void main(String[] args) {

        Student s1= new Student();
        s1.name = "Shivam";
        s1.age = 24;
        s1.clgName = "SMVEC";

        Student s2= new Student();
        s2.name = "Shivfwefwevwvam";
        s2.age = 23224;

        s1.printInfo();
        s2.printInfo();




        // Horse h1 = new Horse();

        // h1.walk();

        // // Ani/mal a1 = new Animal();
        
        // // a1.eat;
        
        
        // Cats c1 = new Cats();
        // c1.eat();


        // // Student s1 = new Student();

        // // s1.name = "Shivam";

        // // // s1.email = "bansal.shivam1216@gmail.com";

        // // s1.setPassword("checking");
        // // System.out.println(s1.getPassword("bansal.shivam12216@gmail.com"));

        // // // Shape s1 = new Shape();
        // // Triangle t1 = new Triangle();

        // t1.area(6, 3);

        // Equilateral e1 = new Equilateral();
        // e1.area(5, 5, 100);
    
// // Polymorphism
    //     Student s1 = new Student();
    //     s1.printInfo("Shivam", 24);

    //     Animal a1 = new Animal();
    //     a1.sound();

    //     Animal a2 = new Dog();
    //     a2.sound();

    //     Animal a3 = new Cat();
    //     a3.sound();

// Inheritance



    }
}