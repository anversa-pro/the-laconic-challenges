using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Test
{
    internal class Program
    {
        static void Main(string[] args)
        {
            String[] A = { "sander", "amy", "ann", "michael" };
            String[] B = { "123456789", "234567890", "789123456", "123123123" };
            String P = "";

            var contacts = new List<string> { };
            int index = 0;
            foreach (var number in B)
            {
                bool contain = number.Contains(P);
                if (contain)
                {
                    contacts.Add(A[index]);
                }
                index++;
            }
            if (contacts.Count < 1)
                Console.WriteLine("NO CONTACT");
            else
            {
                contacts.Sort();
                var contact = contacts.OrderBy(x => x.Length).FirstOrDefault();

                Console.WriteLine(contact);
            }
        }
    }
}


