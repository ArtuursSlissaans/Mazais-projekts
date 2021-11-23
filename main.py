#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>
using namespace std;

void rules();

int main()
{
    string name;
    int amnt; 
    int bidamnt;
    int guess;
    int dice; 
    char choice;

    srand(time(0)); // Use for Generating Random Number Each Time.

    cout <<"\nIevadiet savu vārdu: ";
    getline(cin, name);

    cout <<"\nIevadiet cik daudz naudu jūs gribat tērāt kopumā: $";
    cin >> amnt;
   
    do
    {
        system("cls");
        rules();
        do
        {
            cout <<"\nWelcome "<<name<<" Vai jūs esat gatavs spēlēt? "<<"\n\n"; 
 cout<<"Ievadiet cik liela ir jūsu likme: $";
            cin >> bidamnt;
            if(bidamnt > amnt)
                cout <<"Jūs nevarat likt lielāku likmi nekā jums ir kopupā naudas\n"
                       <<"\nIevadiet jūsu likmi pa jaunu: ";
        }while(bidamnt > amnt);

        do
        {
            cout <<"Uzmini numuru no 1 līdz 10 :";
            cin >> guess;
            if(guess <= 0 || guess > 10)
                cout << "\nNumuram ir jābūt no 1 līdz 10\n"
                    <<"\nMiniet numuru atkal: ";
        }while(guess <= 0 || guess > 10);

        dice = rand()%10 + 1;
   
        if(dice == guess)
        {
            cout <<"\nApsveicu jūs esat uzvarējis :) " << bidamnt * 10<<"$";
            amnt = amnt + bidamnt * 10;
        }
        else
        {
            cout << "Jūs esat zaudējis :( "<< bidamnt <<"$\n";
            amnt = amnt - bidamnt;
        }

        cout << "\nPareizais cipars bija: " << dice <<"\n";
        cout << "\n"<<name<<", Tavs atlikušāis naudas skaits ir " << amnt << "$\n";
        if(amnt == 0)
        {
            cout << "\nJums nav pietiekami naudas lai spēlētu! \n";
            break;
        }
        cout << "\nJa gribi spēlēt velreiz spied y ja nē tad spied n (y/n)? "; 
        cin >> choice;
    }while(choice =='Y'|| choice=='y');
   
    cout<<"\n===============================================================================================\n";
    cout << "Pladies ka jūs spēlējat vēlreiz jūsu atlikušais naudas daudzums ir: " << amnt << "$";
    cout<<"\n===============================================================================================\n";

    return 0;
}

void rules()
{
    system("cls");
    cout<<"\n===============================================================================================\n";
    cout << "\t\t\tSpeles noteikumi";
    cout<<"\n===============================================================================================";
    cout << "\n1. Izvēlies ciparu no 1 līdz 10";
    cout << "\n2. Jūs uzvarēsiet 10 reizes lielāk jūsu likmi";
    cout << "\n3. Jūs zaudēsiet tik cik ir jūsu likme";
    cout << "\n4. Jūs varat iziet ārā no spēlēs jabkurā laikā";
    cout<<"\n===============================================================================================\n";
}

