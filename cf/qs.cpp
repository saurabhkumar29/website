#include<fstream>
#include<iostream>
#include<string.h>
#include<stdlib.h> 
#include<omp.h>
using namespace std;

int k = 0;
class satish
{
int partition(int a[],int l,int h)
{
  int i,j,temp,key;
  key = a[l];
  i = l + 1;
  j = h;

  while(1)
  {
    while((i < h) && (key >= a[i])) 
      i++;

    while(key < a[j]) 
      j--;

    if(i<j)
    {
      temp = a[i];
      a[i] = a[j];
      a[j] = temp;
    }
    else 
    {
      temp = a[l];
      a[l] = a[j];
      a[j] = temp;
      return j;
    }
  }
}

void quicksort(int a[],int l,int h) 
{
  int j;

    if(l<h)
    {
      j = partition(a,l,h);
      cout<<"Pivot element "<<j<<"has been found out by thread "<<k<<"\n\n";

      #pragma omp parallel sections 
      {
        #pragma omp section
        {
          k++;
          quicksort(a,l,j-1);
        }

        #pragma omp section
        {
          k++;
          quicksort(a,j+1,h);
        }
      }
    }
}
}obj;
int main()
{
  ifstream xmlFile;
  xmlFile.open("quickSort.xml");
  char data[500];
  int a[100];
  int i = 0,n = 0;

  xmlFile >> data;  

  xmlFile >> data; 
 
  while(strcmp(data,"</array>") != 0)
  {
    xmlFile >> data; 
    a[i++] = atoi(data);
    n++;  
    xmlFile >> data;
    xmlFile >> data;
  }

  xmlFile.close();

  obj.quicksort(a,0,n-1);

  cout<<"\n\nAfter sorting using quick sort we get : \n";
  for(i=0;i<n;i++)
    cout<<a[i]<<"\t";

    cout<<"\n";
    return 0;
}


......qs.xml.......

<array>
<item>
9
</item>
<item>
7
</item>
<item>
3
</item>
<item>
23
</item>
<item>
4
</item>
<item>
5
</item>
</array>
