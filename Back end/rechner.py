import math

liste_a_maedchen = [3.64800, 3.99800, 4.00620, 2.02320, 1.80000, 1, 1.75000, 0.88070, 1.09350, 1.27900, 1.08500, 1.41490, 2.02320]
liste_a_jungen = [3.79000, 4.10000, 4.34100, 2.32500, 2.15800, 1.78400, 1.70000, 0.84100, 1.15028, 1.42500, 1.59500, 1.93600, 2.80000]
liste_c_maedchen = [0.00660, 0.00660, 0.00656, 0.00647, 0.00540, 1, 0.00500, 0.00068, 0.00208, 0.00398, 0.00921, 0.01039, 0.00874]
liste_c_jungen = [0.00690, 0.00664, 0.00676, 0.00644, 0.00600, 0.00600, 0.00580, 0.00080, 0.00219, 0.00370, 0.009125, 0.01240, 0.01100]
zuschlag = [0.24, 0.14]
handgestoppt = True
z = 0

def punkterechner(geschlecht, D, M):

    if geschlecht == 'weiblich':

        match D:
                
            case '50':
                     
                     a = liste_a_maedchen[0]
                     
                     c = liste_c_maedchen[0]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]
            
            case '75':
                     
                     a = liste_a_maedchen[1]
                     
                     c = liste_c_maedchen[1]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]

            case '100':
                     
                     a = liste_a_maedchen[2]
                     
                     c = liste_c_maedchen[2]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]
            
            case '800':
                     
                     a = liste_a_maedchen[3]
                     
                     c = liste_c_maedchen[3]

            case '1000':
                     
                     a = liste_a_maedchen[4]
                     
                     c = liste_c_maedchen[4]

            case '2000':
                     
                     a = liste_a_maedchen[5]
                    
                     c = liste_c_maedchen[5]
            
            case '3000':
                     
                     a = liste_a_maedchen[6]
                     
                     c = liste_c_maedchen[6]

            case 'hochsprung':
                     
                     a = liste_a_maedchen[7]
                     
                     c = liste_c_maedchen[7]

            case 'weitsprung':
                     
                     a = liste_a_maedchen[8]
                     
                     c = liste_c_maedchen[8]

            case 'kugelstoss':
                     
                     a = liste_a_maedchen[9]
                     
                     c = liste_c_maedchen[9]

            case 'schleuderball':
                     
                     a = liste_a_maedchen[10]
                     
                     c = liste_c_maedchen[10]

            case '200wurf':
                     
                     a = liste_a_maedchen[11]
                     
                     c = liste_c_maedchen[11]

            case '80wurf':
                     
                     a = liste_a_maedchen[12]
                     
                     c = liste_c_maedchen[12]
                 
    elif geschlecht == 'maennlich':
        
        match D:
                
            case '50':
                     
                     a = liste_a_jungen[0]
                     
                     c = liste_c_jungen[0]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]
            
            case '75':
                     
                     a = liste_a_jungen[1]
                     
                     c = liste_c_jungen[1]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]

            case '100':
                     
                     a = liste_a_jungen[2]
                     
                     c = liste_c_jungen[2]

                     if handgestoppt == True:
                          
                          z = zuschlag[0]
            
            case '800':
                     
                     a = liste_a_jungen[3]
                     
                     c = liste_c_jungen[3]

            case '1000':
                     
                     a = liste_a_jungen[4]
                     
                     c = liste_c_jungen[4]

            case '2000':
                     
                     a = liste_a_jungen[5]
                    
                     c = liste_c_jungen[5]
            
            case '3000':
                     
                     a = liste_a_jungen[6]
                     
                     c = liste_c_jungen[6]

            case 'hochsprung':
                     
                     a = liste_a_jungen[7]
                     
                     c = liste_c_jungen[7]

            case 'weitsprung':
                     
                     a = liste_a_jungen[8]
                     
                     c = liste_c_jungen[8]

            case 'kugelstoss':
                     
                     a = liste_a_jungen[9]
                     
                     c = liste_c_jungen[9]

            case 'schleuderball':
                     
                     a = liste_a_jungen[10]
                     
                     c = liste_c_jungen[10]

            case '200wurf':
                     
                     a = liste_a_jungen[11]
                     
                     c = liste_c_jungen[11]

            case '80wurf':
                     
                     a = liste_a_jungen[12]
                     
                     c = liste_c_jungen[12]

        


            


                

