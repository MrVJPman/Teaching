import java.lang.Runnable;

class Racer implements Runnable {
  private String name;

  public Racer(String name) {
    this.name = name;
  }

  public void run() {
      try {
        Thread.sleep(100);
        System.out.print(name);
      }
    catch (InterruptedException e) {} 
    }
  }

class Main  {
    public static void main(String [] args) throws InterruptedException {
      Thread t1 = new Thread(new Racer("1"));
      Thread t2 = new Thread(new Racer("2"));
      Thread t3 = new Thread(new Racer("3"));
      Thread t4 = new Thread(new Racer("4"));
      Thread t5 = new Thread(new Racer("5"));

      //Only t5, t3, t1 can be one of the possible threads that start it off
      t5.start(); //.start() calls run()
      t3.start();
      t1.start();
      t3.join(); //.join() waits for threads to die
      t2.start();
      t1.join();
      t4.start();
      t2.join();
      t4.join();
      t5.join();
    }
}