package a2_1801040104;

import java.util.Iterator;
import java.util.NoSuchElementException;
import java.util.Vector;
import java.lang.Comparable;
import utils.DOpt;
import utils.DomainConstraint;
import utils.EmptyException;
import utils.OptType;

/**
 * @overview Sorteds are mutable, unbounded ss of Customers.
 * @attributes 
 *   Customer   Comparable<Object>  Vector<Object>
 * @object A typical Sorteds object is c={x1,...,xn}, where x1,...,xn are
 *  Customers.
 * @abstract_properties
 * 
 * 
 * @author dmle
 */
public class SortedSet {
	@DomainConstraint(type = "Vector", optional = false)
	private Vector<Comparable> elements;
	
	// constructor methods
	  /**
	   * @effects initialise <tt>this</tt> to be empty
	   */
	public SortedSet() {
		elements =  new Vector<Comparable>();
	}
	
	/**
	   * @modifies <tt>this</tt>
	   * @effects <pre>
	   *   if x is already in this 
	   *     do nothing 
	   *   else 
	   *     add x to this, i.e., this_post = this + {x}</pre>
	   */
	  @DOpt(type=OptType.MutatorAdd)
	  public void insert(Comparable x) {
	    if (getIndex(x) < 0) {
	    	elements.add(x); 
	      }
	    sort(); 
	  }
	  
	  public void sort() {
		  int n = size();
		  Comparable temp;
		  for (int i = 0; i< n-1;i++) {
			  for (int j = 0; j<(n-i-1);j++) {
//				  Comparable o1 = (Comparable)gets()[j];
//				  Comparable o2 = (Comparable)gets()[j+1];
				  Comparable o1 =  elements.get(j);
				  Comparable o2 = elements.get(j+1);
				  if (o1.compareTo(o2)>0 ) {
					  temp = elements.get(j);
					  elements.set(j, elements.get(j+1));
					  elements.set(j+1, temp);
				  }
			  }
		  } 
	  }
	  
	  /**
	   * @modifies <tt>this</tt>
	   * @effects <pre>
	   *   if x is not in this 
	   *     do nothing 
	   *   else 
	   *     remove x from this, i.e. 
	   *     this_post = this - {x}</pre>
	   */
	  @DOpt(type=OptType.MutatorRemove)
	  public void remove(Comparable x) {
	    int i = getIndex(x);
	    if (i < 0)
	      return;
	    elements.set(i, elements.lastElement());
	    elements.remove(elements.size() - 1);
	  }
	  
	  /**
	   * @effects <pre>
	   *  if x is in this 
	   *    return true 
	   *  else 
	   *    return false</pre>
	   */
	  @DOpt(type=OptType.ObserverContains)
	  public boolean isIn(Comparable x) {
	    return (getIndex(x) >= 0);
	  }
	  
	  /**
	   * @effects return the cardinality of <tt>this</tt>
	   */
	  @DOpt(type=OptType.ObserverSize)
	  public int size() {
	    return elements.size();
	  }
	  
	  /**
	   * @effects
	   *  if this is not empty
	   *    return array Comparable[] of s of this
	   *  else 
	   *    return null 
	   */
	  @DOpt(type=OptType.Observer)  
	  public Comparable[] gets() {
	    if (size() == 0)
	      return null;
	    else
	      return elements.toArray(new Comparable[size()]);
	  }
	  /**
	   * @effects <pre>
	   *  if this is empty 
	   *    throw an IllegalStateException
	   *  else 
	   *    return an arbitrary element of this</pre>
	   */
	  public Comparable choose() throws IllegalStateException {
	    if (size() == 0)
	      throw new IllegalStateException("SortedSet.choose: set is empty");
	    return (Comparable)elements.lastElement();
	  }

	  /**
	   * @effects <pre>
	   *  if x is in this 
	   *    return the index where x appears 
	   *  else 
	   *    return -1</pre>
	   */
	  private int getIndex(Comparable x) {
	    for (int i = 0; i < elements.size(); i++) {
	      if (x == elements.get(i))
	        return i;
	    }

	    return -1;
	  }
	  
	  @Override
	  public String toString() {
	    if (size() == 0) {
	      return "SortedSet:{ }";
	    }
	    String string = "SortedSet:{" + elements.elementAt(0).toString();
	    for (int i = 1; i < size(); i++) {
	      string = string + " , " + elements.elementAt(i).toString();
	    }

	    return string + "}";
	  }

	  public boolean equals(Comparable o) {
	    if (!(o instanceof SortedSet))
	      return false;

	    // use Vector.equals to compare s
	    return elements.equals(((SortedSet)o).elements);
	  }
	  
	  /**
	   * @effects <pre>
	   *   if this satisfies abstract properties
	   *     return true 
	   *   else
	   *     return false</pre>
	   */
	  public boolean repOK() {
	    if (elements == null)
	      return false;

	    for (int i = 0; i < elements.size(); i++) {
	      Comparable x = elements.get(i); 

	      /* omitted due to the use of generic
	      if (!(x instanceof Comparable))
	        return false;
	      */

	      for (int j = i + 1; j < elements.size(); j++) {
	        if (elements.get(j).equals(x))
	          return false;
	      }
	    }
	    return true;
	  }
	  /**
	   * @effects <pre>
	   *  if this is empty 
	   *     throw EmptyException
	   *   else 
	   *     return a generator that will produce all 
	   *     the elements of this in sequence.</pre>
	   *
	   * @requires <tt>this</tt> must not be modified 
	   *            while the generator is in use
	   */
	  @DOpt(type=OptType.ObserverIterator)
	  public Iterator iterator() throws EmptyException {
	    if (size() == 0)
	      throw new EmptyException("LinkedList.iterator");
	    
	    return new SortedSetGen();
	  }
	  /**
		 * @overview An inner class that implements the Iterator interface
		 * @attribute
		 * ind Integer int
		 * @object
		 * A typical SortedSetGen is SortedSetGen {currentElements, elements}
		 * where currentElements(currentElements), elements(elements)
		 * @abstract_properties
		 * mutable(ind) = false /\ optional(ind) = false /\
		 * min(ind) = 0 /\
		 */
	 private class SortedSetGen implements Iterator<Comparable> {
		    @DomainConstraint(type="Integer",mutable=false,min=0)
		    private int ind;
		    
		    public SortedSetGen() {
		      ind = 0;
		    }
		    
		    @Override
		    public boolean hasNext() {
		      return ind < size();
		    }
		    
		    @Override
		    public Comparable next() throws NoSuchElementException {
		      if (hasNext()) {
		        Comparable next = gets()[ind];
		        ind++;
		        return next;
		      }

		      throw new NoSuchElementException("SortedSet.iterator");
		    }
		    
		    @Override
		    public void remove() {
		      // do nothing
		    }
		  }
}
