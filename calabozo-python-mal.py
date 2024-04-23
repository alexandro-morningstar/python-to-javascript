import time
import random
import os

# -------------------- FUNCIONES DE DIBUJO ----------------------

def line():
    print("-----------------------------------------------------------------------------------------")

def skull_URD():
    print("""\n
MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMOc;;;;;;;;;;;;;;;;;;;:kWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMWNNNNXXNNNNXl.                    :KNNNNNNNNNNWMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMMMMMMMK:...........;ooooooooooooooooooo:...........;0MMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMMMMNkoooo:.  ........;OMMMMMMMMMMMMMMMMMMM0:...........;ooookNMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMWNXO,        :KNNNNNNNWMMMMMMMMMMMMMMMMMMMWNNNNNNNNNNXc     .xXNWMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMMMMNl..   .ldddx0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKxdddo'..cXMMMMMMMMMMMMMMMM
MMMMMMMMMMMMMMMMWOl:.   .,oXMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:  .:lkNMMMMMMMMMMMMM
MMMMMMMMMMMMMMN0O;     ,0WWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMX:     'k0XWMMMMMMMMMM
MMMMMMMMMMMMMWo.    .lk0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWKko.    .lNMMMMMMMMMM
MMMMMMMMMMMMMWl   ';oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNd;'   .;ckWMMMMMMM
MMMMMMMMMMMX0k;  'OWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMW0'     lNMMMMMMM
MMMMMMMMMMWx. .lO0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM0'     cNWMMMMMM
MMMMMMMMMMWd. .xMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMXd:,   .,:kWMMMM
MMMMMMMMXkx:..'kMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.     oWMMMM
MMMMMMMMx.  c0KNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.     lXNWMM
MMMMMMMMx. .dWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMO.     .';kWM
MMMMMMMMO,..;ooddddokNMMMMMMMMMMMMMMMXxdxXMMMMMMMMMMMMMNOdd0WMMMMMMMMMMMMMMMMMMMMMMMNko:.       .dWM
MMMMMMMMN0k:        .xXNWMMMMMMMMMWNXo. .xMMMMMMMNXXXXXO,  ;0XNWMMMMMMMMMMMMMMMMMMMMK,          .dWM
MMMMMMMMk'..:ddddddo,..cXMMMMMMMMM0;..;oxXMMMMMMNo......    ..cXMMMMMMMMMMMMMMMMMMMMK,          .dWM
MMMMMKoc,.,c0MMMMMMNd,,oXMMMMMMMMM0c';kWMMMMMMMMNd,,,,,,,,.   .:lOWMMMMMMMMMMMMMMMMMK,           ,lo
MMMMMk.  oNWMMNKKKKKXNWWMMMMMMMMMMMWWWWMWNKKKKKKKKXNWWWWWWO'     lNNKKKNMMMMNKKXWMMMK,              
MMMMMk. .dWMMNo.....:KMMMMMMMMMMMMMMMMMMNl.......;d0MMMMMMNOxl.  lNk'..xMMMNo..;0MMMK,              
MMXdc,',:OWKo:.     .;cxNXdcckWMMMMMM0oc:.       ..;cdXMMMMMMO'  .:,.,:OMMMNc  '0MMMK,              
MMO.  lNX0Oc.          ,K0'  cNMMMMMMx.              .dOKWMMM0'    .dNWMMX0k;  ,0WX0d.              
MMO.  lWO.             ,K0'  cNMMMMMMx.                 cXMMMO.  ;xOXMMMNo. .lk0NX:                 
MMO.  lWk.             ,K0'  cNMMMMMMx.                 :XMMMO.  lNMMWO:;.  .OMMMX;                 
MMO.  lWk.             ,K0'  cNMMMMMMx.                 :XMMM0,..;xkkx;    .,0WKkd.                 
MMO.  lWk.             ,K0'  cNMMMMMMx.                 :XMMMWK0l.       .o0KXK:                    
MMO.  lWk.             ,K0'  cNMMMMMMx.                 :XMMMMMMk.     ,cdKWx;'.                    
MMO.  lWk.             .ll'..oNMMMMMMx.                 :XMMMMMMk.   .'kWKxo,                     .'
NXx.  lWk.                ,k0XWMMMMMMx.                 ;0NWMMMMk.  ;k0KKc                       lKX
c..'lo0Wk.             .cc'.'oNMMMMMMx.                  .'oNMMMk.  ......                       dWM
'  cNXxo;            ..,lc.  :NMMMMMMO;..                  :XMMMk.                               dWM
'  :Nk.             'OXo     :NMMMMMMWNXo                  ;XMMMk.                              .dWM
'  cNk.             ,KWd.    :XMMMMMMMMWd                  :XMMMk.                            ,dxKMM
'  :N0:,.         .'':l'     .coOWMMMMMMO;'.             ',dNMMMk.                            oWMMMM
,  ;k0XNx.       ,OXc           lWMMMN0O0XNl.           ;KX0O0XMk.                           .oWMMMM
0kl. .oNXOx;  .lk0WNl           lWMMMk. .xWXkkkkkkkkkkkk0WO' .dWNOkc.                      :kOXMMMMM
MMXo:,';;;;'':oKMMMNl   ,,.     lWMMM0l;'':oKMMMMMMMMMMXo:,';cOWMMM0l;.              .;:::l0MMMMMMMM
MMMMMO'.   .dWMMMMMNo. ,0K;    .oWMMMMMWd. 'OWKOkkkkkkko. .oNMMMMMMMWWd.         ....:XMMMMMMMMMMMMM
MMMMMNKOc  .xMMMMMMMX0OKWWK0OOO0XMMMMMMMN00KWNc         .d0XMMMMMMMMWNo        .d0000XWMMMMMMMMMMMMM
MMMMM0:,',co0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMWkcccccccccxNMMMMMMMMM0c,',cccccccdXMMMMMMMMMMMMMMMMMMM
MMMMMx. .dWKxxONW0xx0NNOxx0WNOxkKWXkxkXWKkxkNWKxxxxxxxxxxxxxxxxxxxxc..'kWMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMx. .oKc  'kK;  ,0O'  :Kk.  lXd. .oXl  .xXc                     c0KNMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMKdl,...;c,...:c'..'c:'..'c;.'.,c;.'.;l,...  .':lllllllllllllllo0WMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWo  .kNc  '0X;  ;X0'  cNO.  oWx. .xWo     'o0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWo  .kNc  '0X;  ;X0'  cNO.  oWx. .xWo     'o0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWo  .kNc  '0X;  ;X0'  cNO.  oWx. .xWo  .:dk0NMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMWk,..;c,...:c'..'c:'..'c:...,l;...;l,.':0MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMWNXc  'k0;  ;0O'  :Kk.  lXd. .dXl. .xNNWMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
MMMMMMMMMMWOc:dXNxc:xNXd:ckWXo:cOW0l:l0WOl:oKMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM
          """)
    
def creature_1_100():
    print("""\n
                                 .:do,...cxlc;'..';:,.                                              
                               .:do,.  ...,.      .,do:'                                            
                             ,od:.                   .:c:;,.                                        
                           .:dc.                       ..';::;.                                     
                          .lo'                           .  .'::'                                   
                         .lxc'..;;.                       ..   .',,.                                
                        ,xOxl;,,,'.              .','.        .. .,lc;.                             
                      'dkOk:.                    ..'co:.          ...;ol'                           
                     ;ddxx;.                        .,clc;.        .  .:o:.                         
                   .lxldd,                             .;lcc:,.       ...,::.                       
                  .ox:ld,                                ...,::;,',,,'....'cdl'                     
                  ,xloo'                                   ... .....',''',;;lxd:,,..                
                 'oxc'.   .;::,;;;;:odl'.                    ...             ...,::;;;'.''.         
               'ldc.    .:oc'..     .;do'...                .'::;:cc;,'..       .....,,':l'         
            .:cc:.     .co;..         .ll. .           .;c:;:c,.  .;ldxxo:''..'..;c'... .:'         
          .;do'      .ckxc.            .;c,....''''';cllc,.   .       ..':l;.    'c.   .:l.         
         'ld:.     ..:0k;.               :dllcc:;,'''..          ..       'oxc. .:;.  .;xk:.        
        ,dl.      ..;dx;..''.    ....   .ld:.                               'od:cl.  .cl,cxc.       
      .;l:.      ;ol,,:' .....    ..'. .::..                                 .;oo;.  ;c. .'lc.      
    ..cl,     .,cl;. .:'.             'l:...                               .. .lc..'ol'    .cc.     
  ,l:;,.   .'ldc.     ,c'...     ..'..cl...                                .  cx;.'dd'  .  'ol.     
 .:l;.   .cdl;.       .lc,,,,,,,,;;'.,o:..                               .   :xc..co'   .ldo;.      
   .,ol'..ld;.         ,oc'..,;;,...;ol'.                              ..   ,xl.,xk:.   .lxl'       
     cOc.  ,o:.         'od;.... .,od:..                              ..   ;dl.'loxo'     .,;l:.    
    ..:c.   .c:.         .:xo. .,cl;.                                    .lk:.;c'.'::,;:'  .'oOkc.  
     ..,c;.   ;c'          'llcl:..                          ..,clc:,''';ll''co,      .,lc;cldOOxd;.
.      ..::.   ,c,.          ..                             ..'xOkxc'. ... .c:.      .. .:oooodkkd:.
 .      ..co,   'l;                                          .oOl,.cl. .  ;o;           ..'cloc;;...
  ..     ..,c:.  .c:.                                        .;,...:dccc',o;             .. ...  ...
   ..     . .,l;. .lo'                                        ....:kd:xOdod:.             ...   ... 
     ..    .  'oc. .;c'                                         .d0o,,kkx0Od'               ..  ..  
       .. .'::cc,    ,:.                                        ;Ol. .dkx0OOl.                      
       .:dk00Oko;',;,:c.                                        ;l.  .cldkdko.                      
    .;oOOKX0OOXOc'.lkd;                                         ..    ..:d,cx;                      
  .lkKXKOxxkkkx:..:xOl.                                                 .. 'l,                      
..xKxoOKOcckOd;..lxl;.                                                                              
..;:''xOc':xx:.....                                                                                 
......,'...cd;...                                                                                   
 ...   ..  ..                                                                                       
..    ...                                                                                           
      ..                                                                                            
     ..                                                                                               
        """)

def cara_nino_100():
    print("""\n                                                                                
                                                       ......                                       
                                                .....                                               
                                                                                                    
                                       ....          ........                                       
                                 ...............       .............                                
                                ....................   ..................                           
                            ....  ... ............................... .......                       
                           ....      .........................................                      
                 ......      .................................................                      
               ....          ...................................................   .   ..           
             ...            .....................................................  ......           
            ..    ...   ..........................................................  ......          
          ...    ....  ......  .... .....  ...........................................  ...         
         ...         .......  ..................................   .........  ................      
        ....    ...     ...  .............................  ...  ..........    ................     
      .....     ...    .............. ..................... ...  ...........     ......  ....  .    
      .....   ....     .............  .....................  .    ..........       ..........       
    ..      ... ..       ...........  ......    ......   ...   .  ...........     ...............   
    ..          ..      .......  ...........    ...  ...  ... ..  ............    ..... .........   
   ..   ..      .      ..   ..  .... ....... .. .... ........... .............      .... .......... 
   ..  ...  .    ..             ...   .....  ..................  ............. .    ............... 
      ...  ..                 .....  ... ...... .......  .....  .............  ..     ............  
      ... ..                 ...   ............  ...... ...................... ....    ...........  
     ...  ..     .  .         ...  ........ .................................  .  ...   ..........  
 .    ..  ..       ...    .......  ..........................................  ......   ..........  
 ..  .......       ...    ... .....................................................      ........   
 ... .   ...       ..      ..  ......................................................    .......    
  ....    ..       ..    .... ........................................................ .. .....     
   ....   ..       ..   ..... ........................................................  .. ...      
     .... ..       .. ............          ..........................................     ..       
        ....          .........               .........................  .............     .        
              ...     ........                 .....................          .......               
             .....    .......                   ...................              ...                
             .....   ........                    ...............                  ..                
             ......  ........                    ..............                  ..    ..           
               ....   .......                    ..............                  ..    ...          
                 ...    ......                 ..................               ....    .           
                        ........             .....................             ....                 
                        .............    ..........................           ....                  
                         ............................................... .........                  
                         ...................................................   ..                   
                          ................................................     .                    
                           ......................................................                   
                           .....................................................                    
                            ...................................................                     
                             .................................................                      
                               ........................     ..................                      
                                .........................  ..................                       
                                  .........................................                         
                                    ....................................                            
                                        .............................                               
                                            ......................                                  
                                                 ........  ... .                                    
                                                                                                    
  
        """)
    
def scary_face_150():
    print("""
                                                           ..             .   .                .
                                                         ..  ....................     ....... ....
                                                    . ...  ..           .    ..         ..    ..
                                                     ..........   ....  .    ...   ...     .. ...
                                                   .    ..  .     ....        . .. ...  .    ...
                                             .     ..        . ......    ...  . ...       .....   ...
                                             .. ..  ..          ...       .      ...       ....
                                             ........................          .....      ......   .
                                                 ..... .....    .              ....  .            .
                                           .. .........    .                   ...      . .........   .
                                          ....   ......     ..                           .........   .     .
                                          ....   .                                       ..... ...  .     .
                                          ...... ...                                                      
                                         ..........                   ..'..                    .....    
                                       .      ....                .,:okXNXx'                  . ..  ....  
                                       ..     ...                .kXNWWWWWWk'                 ..    ..  .
                                      ..   .                   .;kNWWWWWNKNWd.     .lxxxo,.    ... ... . 
                                       .....                   cXWWWWWWWXxoo;     .dXWWWKc.    ......... 
                                     .. ...  .                 lNWWWWWWXk:.       cNWWWWXd.  ......        
                                         ...                   ,ONWWWWNd.      .  cXXNWWW0, .......       
                                         ....                  :XWWWNOc..         ':c0WWWO'  ..     .     
                                         .  .                 .xXOxdc...            'OWWWO'  .       .    
                                        ... .                 'c,.            .     ,0WWWO'  .   .        
                                           .                                 ..     .lKWWO,      ..      
                                        .                                 ..  ...    .lXW0,.    ..       
                                                                  .......,kOoldk:    ..'xx,.   ..         
                                                  .               .:dKKKKKNWK0KOkc   .  ...    .         
                                                 ...             .:d0WWWWWWWWXKNNl   ..   .               
                                               .                 ,0WWWWWNWW00KxxOc   .....   .          
                                                                 '0WWWWKkxxOXWN0c.  . ..                 
                                                       .  .      .xXNWWXxl:kWWWXc  ..      ..          
                                                     .   ..       'cOWWNk:cokNWK:.    .    .           
                                ...            ..       ...      .:d0WWXxod;cNKc..                      
                           .   .               ..        .       ,0MWWWWXOOO0Xk'                     
                       . ...                  ..          ...... ,0MWWWWWXldWXo.                       
                   .                      .   .            .  .. ,0MWKKWNOloK0c.             .         
            . ...                         .                  ... ;KMW00Nk:k0d;...                    
                                         .                       ;0X0KWO,'kWd. .                     
       .                                                         ;0NKXWk,;dl.    .                    
   ...                                                 ..        ,ONWW0;:k:    .                     .  
  ..                                                   ..       '::lOWd.,k:  ..                      .  
                                                      .        :Od'.,dc.'o; .                         .
                                                              .od.   ..  ..                            
                                     .                       .,:..                                     
""")
    
def face_hands():
    print("""
                                                            ...                                                ......          ...     ..        
                                                            ..                                                 ..  ..          ...     ...       
                                                           ..                                          ..      ..   ...        ....    ...       
                                                          ...                                         .....     ..     ...     ....     ...      
                                                          ..                                          ......     ..     ...    .....     ..      
                                                         ...                                           ..  ..     ...     ...  ..  ..    ..      
                                                        ...                                            ..   ...    ...     ... ...  ...  ...     
                                                       ...                                              ..   ...     ..     ......   ...  ..     
                                                       ..          ........                  ....       ..     ..     ..     ......   ......     
                                                       ..        ...     ...                ... ....     ..     ...    ..      .....    ....     
                                                       ..       ...      ..                  ..    ..... ...     ...    ..      .....     ...    
                                                       ..      ...       ..   ........       ..       .......      ..   ..       .....     ..    
                                                       ..      ..       .......     ..        ..       .......     ..   ...        ...     ..    
                                                       ..     ..     .......      ....        ....      .......     ..   ..         ...    ..    
                                                      ...     ..     .....      ....            ...       ......    ..   ..          ..    ..    
                                                    ......    ..    ...       ....   ..,ccccccc'.....      ......    ..  ..          ..    ..    
                                                    ..  ...  ..   ...       .... .;lx00NMMMMMMWXk:.....      ....    ..   ..         ..    ..    
                                                    ..   ..  ..  ...      ...    lNMMMNXXNWMMMMMW0,  ...        ...   ..  ..              ..     
                                                    ..   ...... ...      ...    ;0MMNkc,,;l0MMMMWk'    ...         ..........             ..     
                                                    ...   ........     ...      dMWO:.....c0MMMMW0,     .....         ...                 ..     
                                                    ....  .......     ...       dWNd,...'xNMMMMMMX:   ........                            ..     
                                                ......... ......      ..        ,kNNKx:,xNMMMMMWXd'....    ....                           ..     
                                             .....     ..... ..       ...        .;loOKXNMMMWXKx;...      ..  ..                          ..     
                                            ....        ... ...       ..            ..cOkloOk;'..        ...  ..                          ..     
                                           ...          ......        ..            ...,'..,,..          ..   ..                          ..     
                    ........................            ......        ..             ........          ....  ...                          ..     
                ....................                    ... ...       ...            .....         ....      ..                          ..      
             ......                                    ..    .         ..          .....         ...        ...                         ...      
           .....                                       ..               ..     .....         ....           ..                         ..        
         ....                                          ..               .......            ....             ..                        ...        
        ...                                            ..                 ..            ....           .. ....                      ...          
      ....                                             ..                            ....           ..... ....                     ...           
     ...                                                ..                         ...            ...     ...                  .....             
    ...                                                  ..                     ....            ...      ...              ......                 
   ...                                                    ..                   ...           ....      ....             ......                   
  ...                                                      .                  ..        ......      ......             ... ......                
  ..                                                       ..                ..    .....         ....  ...            ..       .....             
 ...                                                        ...             ........          .....    ..             ..         .......         
 ...                                                         ...            ....           ........   ..            ...              ....        
 ..                                                           ....                       .........   ...           ..                  ....      
 ..                                                             ........               ... .....  .....     .   ....                     ...     
...                                                                ......      ..      ......... .......    ........                      ....   
..                                                                 ...............    ...........................                           ...  
..                                                                  ................ ...........................                             ..  
.                                                                   .........................................                                ... 
.                                                                    ... .................................                                    .. 
                                                                     ...  ..    ..................  ....                                      ...
                                                                          ...       .. ...............                                         ..
                                                                           ..            ...........                                           ..
        """)

def big_mouth_100():
    print("""
                                                          ...........  ....    ....'.....           
                                                       ...'...                       ...'..         
                                                     .''..                               .'..       
                                                  ..''....                                ..'.      
                                                .'''..  ..                                  .'..    
                                               .''..    ...                                  ..'.   
                                              .'..      ..                                     .'.  
                                             .''.      ..                                       .'. 
                                             .'.      ..                                        .'. 
                                            .'.       .                                         .'. 
                                           ...       ..                                         .'' 
                                           .'.      ..                                          .''.
                                           .'.     ..       .......                             .'. 
                                           .'.             .........                            .'. 
                                          .''.             ...........                         .'.  
                                          .'...           ............                        .'.   
                                          .'...            ..........                       .''.    
                                           .''.            .....            ..             ..'.     
                                           .''                              ... .         ....      
                                           .''.                             .........    .''.       
                                          ..'''.                 ....       ..........  .''.        
                                          .'''''.               .'.   ...    ......... .''.         
                                          .''''''..             ... .'','.    .....  ..'..          
                                        ..'''...'..                .''''.           .''.            
                                       ..''...'''.                 .''..          ..'.              
                                       .'''..',,''...               .            .''.               
                                       .',...'..',''..'.....                    .'..                
                                      ..''. ..  .,,...'''''''..            .....'.                  
                                     .','.  ..  .'...','''''.'''..    ....'''''..                   
                                   ..'''..      ...  ...'''...'..''..'''''.'''.                     
                                  .''''.        .      .''.  .'...''''''''''..                      
                                 .'..',.              ...    .'..''...''''.                         
                              ...'.'''''.                     ....  ..''''.                         
                             .',...''...                          ..''''''.                         
                          ...''.. .,'.                          ..''','..'.                         
                     .......... ...'.                         ....''',. .'.                         
                 ...''...       .'''.                            .'''.  ..''.                       
              .......           .'',.                         .''','.      ..'..                    
            ..''.               .'''.                       ..'''''.         ..'..                  
           .''.               ..',,'.                   .   ..'''''.           ..'..                
          .'.               ..'''..                     ..   .''''.              .'..               
         .'.               ..''''.                      ..  .'''''.               .''.              
        .'.               ...'''.                      ..'..''''..                 .....            
       .'.               .. .''.                       .''''''...                    ..''.          
      .'.                . .''..                       .'''''. ..                      ..'..        
      .'.               ...''''.                      ..''''.  .                         ..'.       
     .'.               . .','''.                     .',,''.  ..                           ...      
     ..              .....''''.                      .','''. ..                             .'.     
    .'.              ....''''.                       ..'''. ..                              .'.     
    .'.             .....'''...                     ..''''. .                                .'.    
   .'.              .....''....                   ....'''....                                 .'.   
   .'.             .. .'.''''..                   ....''..''.                                  .'.  
  .'.              .  .'''''.                    ....'''..'.                                   .''. 
  .'.             ......'....                   .',''''','.                                    ..'. 
  .'.             .',..''.                    ...,',''''...                                    .''. 
   ...           ...'''''.                    ...,''''....                                      .''.
   .'.        .. ...''''..                     ..','''. ..                                       .'.
  .'.          .....''.                        .'','',...                                       .'. 
  .'.           .',''.                         .''''''...                                      .'.  
 .'.            .''''.     .                ....'''''...                                       .'.  
.'.             .''...    .                  ...''''. ..                                      .'.   
.'.            .''..''...                   ...'''..  .                                      ...    
.'.           .''''''....         ...     ...''''..                                         .'..    
.'.          .'''''...''.      . .. .     ...'''.                                           '.      
.'.          .''..'..''.  .....  .  .  .  ...''.                                           .'.      
.'.          .'.  .''.. .''.... .. ...''. .'''.                                            .'.      
.'.          ...   .''..'''..''...'....''..'..                                             ..       
.'.          .'.     .'''''..''''''.. .'''''.                                              ..       
 .'.         .'.       ...''''''.','..''..''.                                              ..       
 .'.        .''.           .........    ..'.            ..     .'..                        ..       
 .'.        .''.                       ....            .''.     ......                     ..       
 .'.         .'.                     .''.               ...'.      ........               .'.       
 .'.         .'.                    .''.                  .'''..       ..''''''.'''''... ..'.       
        """)
    
def face_flesh_150():
    print("""
                                                                    .     .....                                                                       
                                                                   ...................                                                                
                                                                  ........................                                                            
                                                           ...................................                                                        
                                                      ...........................................                                                     
                                                      .............................................                                                   
                                                      ..............................................                                                  
                                                    .................................................                                                 
                                                   ...................................................                                                
                                                  .....................................................                                               
                                                 .......................................................                                              
                                                 ........................................................                                             
                                                 .........................................................                                            
                                                 .................. .......................................                                           
                                                 ..............  .........................................                                            
                                                ..............  ...lo. .. ................................                                            
                                                 ............  ......   .       ..............   ........                                             
                                                 ...........   .....    ..         ...........     ......                                             
                                                  .........   ......    ..         ...     ....     .....                                             
                                                  ........    ......    ..         ...     ....     ...                                               
                                                ..........   ........  ...         ...,'.. ...      ....                                              
                                                .. .....     ..;c;........         ......  ..       ...  .                                            
                                                ..  ....     ..:l,........         .........        ...  .                                            
                                                ..  ...      ...........      ..   ........         .    .                                            
                                                 .  ...      .  ..... .       ..   . ......   ..   ..    .                                            
                                                 .  ...      .   ....          .      ...'.       ...   ..                                            
                                                  .. ..      .   ..',.      .  .      ...:'   ..  ...  ...                                            
                                                  ......     ..   ..';.     .  .     .....  ....  ...  ...                                            
                                                   .....          ...,.     ..        ...  ....   .......                                             
                                                    ....       ..  ..       .         .  .,...    .....                                               
                                                      ...      ..''..                ....;c'..    ...                                                 
                                                       ...     ..,'.:'         .....;;'.,l;..     ..                                                  
                                                        ..     .   .:...     .':;..:ko'..:,.;.   .                                                    
                                                        ...    ..      .    .cc:c..::... ...'.   .                                                    
                                                        ...     ..      .   .dc           .,,   .                                                     
                                                        ....      .      ....,l'          .;'  ..                                                     
                                                         ....      ..         .           ..   .                                                      
                                                         ....        .. ,;               ..   ..                                                      
                                                      .......       .  .;,               ..   . ..                                                    
                                                    ..   ...        .   ... .:,   . ';.  ..   .   ..                                                  
                                                 ...     ...        .   .....l;  ':.ld. ..    .   ..                                                  
                                                 .       ..          .  ..  .o;   ..lo.       ...  .                                                  
                                                 ...    ...   .      .  ..  .o; ....,;..   .....   .                                                  
                                                .....  ...            . ..  .;. ....   ......      .                                                  
                                           ........   ....     .      .....  .  ...   .....        .. .                                               
                                       .......             ... .         ..     ........           .......                                            
                                  .........         .          ..        ..... .....                    ........                                      
                                                     .             .,:::c;....;c,.               .          .........                                 
                                                      ..          .oXNNNNKOOkdOXd.             ..                  .....                              
          ........                                     ..         .xNXNNNNNNNNNNk'                                   .....                            
       ..........                                       ..        .xNXNNNNNNNNXNO,        .                                ..  ........               
    ......                                               ....     .lKXNNNNNNNNXNO,      ..                                        ............        
  ..... .                                                  ...     .kNXNNNXNNNXNk'   ..                                             .      .....      
  . ..  .                                                      ..  .kNXNXNNNXNXNk'...                                                      ......     
 ...     .                                                         'kNXNXXXXXNNNO,                                                      .  .   ..     
 ...     .                                                         .lkxxxxxxxxl:,                                                     ..   .   ..     
...                                                                     .                                                           ..    .     ..    
...                                                                     ...                                                       .      .      ...   
...                                                                     ....                                                     .     ..         ..  
 ..                                                                                                                                    .          ..  
 ..                                                                                                                                    .          ... 
...                                                                                                                                   ..           ...
        """)

# -------------------- FUNCIONES LOGICAS ----------------------

# Función que captura una desición de Si o No
def si_no():
    while(True):
        try:
            decision = str(input("(S/N): "))
            if decision == "S" or decision == "s" or decision == "N" or decision == "n":
                break
            else:
                print("Opción inválida, solo se acepta \"s\" o \"n\"")
                continue
        except:
            print("Opción inválida, solo se acepta \"s\" o \"n\"")
    return decision

# Función que captura una desición de Izquierda o Derecha
def left_right():
    while(True):
        try:
            decision = str(input("(I/D): "))
            if decision == "I" or decision == "i" or decision == "D" or decision == "d":
                break
            else:
                print("Opción inválida, solo se acepta \"i\" o \"d\"")
                continue
        except:
            print("Opción inválida, solo se acepta \"i\" o \"d\"")
    return decision

# Función que captura una desición de Planta Alta o Planta Baja
def ds_us():
    while(True):
        try:
            decision = str(input("(H/S): "))
            if decision == "S" or decision == "s" or decision == "H" or decision == "h":
                break
            else:
                print("Opción inválida, solo se acepta \"s\" o \"h\"")
                continue
        except:
            print("Opción inválida, solo se acepta \"s\" o \"h\"")
    return decision

# Función que captura la respuesta de cada acertijo
def riddle():
    while(True):
        try:
            answer = input("Ingresa tu respuesta: ")
            if answer.isdigit():
                answer = int(answer)
                break
            else:
                print("Valor incorrecto, revisa tu respuesta")
        except:
            print("Valor incorrecto, revisa tu respuesta")
    return answer

# Función que genera el inicio del fin
def end():
    line()
    time.sleep(1)
    print("\n Bajas las escaleras, intentas abrir la puerta sin éxito. No puedes creer que la pesadilla aún no termine.")
    time.sleep(1)
    print("\n De pronto tienes las misma sensación... el mismo peligro que sentiste en la cama.")
    time.sleep(1)
    print("\n La puerta no se abrirá... lo único que puedes hacer es voltear.")
    next()
    face_flesh_150()
    next()
    time.sleep(1) #4
    print("\n Aquí está \"él\", te extiende su mano... no estás muy seguro de qué hacer... ¿vale la pena el riesgo?")
    line()

# Función que solicita un Enter para continuar
def next():
    next = input("\n --> Presiona Enter para continuar...")

# -------------------- La Pesadilla ----------------------

while(True):
    title = "Bienvenido a La Pesadilla"
    print("⛧"*len(title*2) + "\n" + title + "\n" + "⛧"*len(title*2))

    print("¿Iniciar el calvario?")
    start = si_no()
    os.system("cls")
    
    # Iniciar o cerrar el juego
    if start == "s" or start == "S":
        moneda_morte = False
        moneda_satana = False
        daga = False
        no_ran_1 = random.randint(1,30)
        no_ran_2 = random.randint(1,30)
        no_ran_3 = random.randint(1,30)

        print("""
              Oye hijo mío, el silencio.
              Es un silencio ondulado, un silencio donde resbalan valles y ecos,
              y que inclina las frentes hacia el suelo.
            """)
        next()
        line()
        print("""
            Despiertas en medio de la noche después de haber caído inconsciente a media pijamada por la cantidad de alcohol que tomaste.
            Recuerdas que la fiesta era en el departamento de uno de tus amigos que se mudó a la gran ciudad.
            Sin embargo, solo hay silencio, no hay sonido de autos, de claxons, no hay luz artificial exterior que penetre la penumbra del cuarto donde estás...
            sabes que estás solo, no sientes la presencia de tus amigos.
            """)
        time.sleep(1)
        line()
        print("¿Te levantas de la cama? ")
        wake_up = si_no()
        os.system("cls")

        if wake_up == "s" or wake_up == "S":
            print("\n Al levantarte de la cama sientes como algo te toma violentamente de los tobillos y quiere arrastrate al fondo.")
            time.sleep(1)
            print("\n Después de forcejear logras librarte apenas.")
            time.sleep(1)
            print("\n Ya conoces la habitación, por lo que huyes a la puerta rogando que lo que sea que se arrastra apresuradamente hacia tí por la espalda no logre alcanzarte.")
            time.sleep(1)
            print("\n Logras salir y cerrar la puerta tras de tí, revisas tus bolsillos y encuentras tu telefono celular con el cual alumbras.")
            time.sleep(1)
            print("\n En el piso, en las paredes, solo humedad y manchas rojizas. Un aire pesado, no sabes que hay a los lados, se te heriza la piel de pensar en que puedes encontrar al voltear. ")
            time.sleep(1)
            print("\n En el piso frente a ti encuentras una moneda de hierro con la inscripción \"in morte ultima veritas. Vincit veritas in omnire\"")
            time.sleep(1)
            line()
            print("\n ¿Tomas la moneda?")
            take_coin_1 = si_no()
            if take_coin_1 == "s" or take_coin_1 == "S":
                moneda_morte = True
                print("\n Tomaste la moneda")

            else:
                moneda_morte = False
                print("\n Ignoraste la moneda")
            next()
            os.system("cls")

            time.sleep(1)
            print("\n Hay dos caminos, izquierda y derecha, tienes el presentimiento de que algo te observa desde la derecha, por el otro lado (izquierda) solo hay un silencio sepulcral...")
            time.sleep(1)
            line()
            print("\n ¿Qué camino eliges?")
            direccion = left_right()
            os.system("cls")

            if direccion == "I" or direccion == "i":
                skull_URD()
                next()
                print("\n Caminas durante unos segundos hasta que entras en razón de la profundidad del pasillo, al querer regresar, no eres capáz de volver al punto inicial...")
                time.sleep(1)
                print("\n Caminas con la esperanza de escapar en algún momento, pero la esperanza sí muere, junto contigo.")
                time.sleep(1)
                print("\n No todo tiene porque ser un aprendizaje, a veces solo se falla y ya...")
                next()
                os.system("cls")
                continue

            else:
                print("\n Caminas por el pasillo. La que en otro momento sería la potente luz flash de tu celular, ahora pareciera no ser más que una vela palpitando en la oscuridad absoluta.")
                time.sleep(1)
                print("\n Tras avanzar apenas un par de metros, repentinamente, frente a ti, sientes un calor y una respiración tan intensa que te petrifica.")
                next()
                creature_1_100()
                next()
                print("\n El sobresalto provoca que sueltes tu fuente de luz.")
                time.sleep(1)
                print("\n Al reincorporarte ya no está frente a ti, ahora solo hay frío...")
                next()
                os.system("cls")
                
        # Desición de no levantarse
        else:
            print("\n Mientras estás recostado buscas tu celular en los bolsillos para alumbrar la habitación.")
            time.sleep(1)
            print("\n La luz confirmaque estás en la habitación de tu amigo, no hay nada extraño a decir verdad.")
            time.sleep(1)
            print("\n Solo ese inquietante silencio, solo esa penumbra que pareciera devorar la luz.")
            time.sleep(1)
            print("\n Te dispones a revisar el carrete para averiguar que sucede, solo hay una foto, una foto borrosa:")
            next()
            cara_nino_100()
            next()
            print("\n Sientes un escalofrío al percibir algo moverse bajo la cama.")
            time.sleep(1)
            line()
            print("\n ¿Quieres revisar bajo la cama?")
            check = si_no()
            os.system("cls")

            if check == "s" or check == "S":
                scary_face_150()
                next()
                print("\n Moriste al ver directacmente a \"él\" ")
                time.sleep(1)
                print("\n \"Maldita sea la noche\"")
                next()
                os.system("cls")
                continue
            
            else:
                face_hands()
                next()
                print("\n Algo te toma por debajo de la cama con sus extremidades animales.")
                time.sleep(1)
                print("\n Ese \"algo\" comienza a hundirte en la cama hasta que te sientes devorado por ella.")
                time.sleep(1)
                print("\n Cierras los ojos esperando que todo esto termine pronto")
                next()
                time.sleep(1)
                print("\n .")
                time.sleep(1)
                print("\n .")
                time.sleep(1)
                print("\n .")
                time.sleep(1)
                print("\n De pronto no hay presión.")
                time.sleep(1)
                print("\n De pronto no hay dolor.")
                time.sleep(1)
                next()
                os.system("cls")
                print("\n Despiertas nuevamente por una gotera en el techo.")
                time.sleep(1)
                print("\n Reconoces este lugar, reconoces el olor a humedad del zótano.")
                time.sleep(1)
                print("\n Esa luz tenue y ese palpitar de la luz te saca de quisio...")
                time.sleep(1)
                print("\n En el suelo ves una moneda de hierro con la inscripción \"Ave Satana, archagele. Ave Satana, salve annus abit\"")
                line()
                time.sleep(1)
                print("\n ¿Quieres tomar la moneda?")
                take_coin_2 = si_no()

                if take_coin_2 == "s" or take_coin_2 == "S":
                    line()
                    moneda_satana = True
                    print("\n Tomaste la moneda")

                else:
                    line()
                    moneda_satana = False
                    print("\n Ignoraste la moneda")

                next()
                os.system("cls")
                time.sleep(1)
                print("\n Miras a tu al rededor, en la esquina está el viejo baúl de tu amigo, un baúl cerrado con un candado de 3 dígitos.")
                time.sleep(1)
                line()
                print("\n ¿Quieres intentar abrir el baúl?")
                open = si_no()
                os.system("cls")

                if open == "s" or open == "S":
                    while(True):
                        print("\n Él siempre decía que amaba las matemáticas.")
                        time.sleep(1)
                        print("\n Pero su mala memoria no lo ayudaba, por eso siempre dejaba acertijos cerca.")
                        next()
                        line()
                        print("\n El coeficiente correspondiente al resultado de la primer derivada de {}x^2".format(no_ran_1))
                        first_number = riddle()
                        os.system("cls"),
                        print("\n El coeficiente correspondiente al resultado de la primer derivada de {}x^2".format(no_ran_2))
                        second_number = riddle()
                        os.system("cls")
                        print("\n El coeficiente correspondiente al resultado de la primer derivada de {}x^2".format(no_ran_3))
                        third_number = riddle()
                        os.system("cls")

                        # Continua AQUI!!!!!!!!!

                        if first_number == no_ran_1 and second_number == no_ran_2 and third_number == no_ran_3:
                            print("\n Encontraste una daga hecha con la mándibula de un carnero y una fotografía que muestra dos monedas.")
                            daga = True
                            break
                        
                        else:
                            line()
                            print("\n Parece que no se ha abierto ¿Quieres intentarlo de nuevo?")
                            again = si_no()
                            os.system("cls")

                            if again == "s" or again == "S":
                                continue
                            
                            else:
                                line()
                                print("\n De cualquier forma no creo que haya algo interesante dentro del baúl.")
                                next()
                                os.system("cls")
                                break
                else:
                    print("\n De cualquier forma no creo que haya algo interesante dentro del baúl.")
                    next()
                    os.system("cls")

                line() # Aqui llegamos, se haya abierto el baul o no.
                time.sleep(1)
                print("\n Sales del cuarto de lavado.")
                time.sleep(1)
                print("\n Te preguntas si es buena idea regresar a la habitación donde despertaste inicialmente.")
                time.sleep(1)
                print("\n O si simplemente deberías ir directo a la salida.")
                line()
                time.sleep(1)
                print("\n ¿Quieres subir a la Habitación (H) o a la Salida (S)?")
                floor = ds_us()
                os.system("cls")

                if floor == "H" or floor == "h":
                    time.sleep(1)
                    print("\n La oscuridad es tan densa que aún con tu celular, no logras ver más allá de un metro por mucho.")
                    time.sleep(1)
                    print("\n Al subir las escaleras escuchas pasos, no sabes qué, pero algo está esperando al final de los escalones...")
                    time.sleep(1)
                    print("\n Ni bien dado el último escalón, sientes un calor y una respiración tan intesa que te petrifica.")
                    next()
                    creature_1_100()
                    next()

                    if daga == True:
                        line()
                        print("\n Recuerdas que tienes la daga...")
                        line()
                        print("\n 'Quieres utilizar la daga? (S/N)")
                        use_knive = si_no()
                        os.system("cls")

                        if use_knive == "S" or use_knive == "s":
                            big_mouth_100()
                            time.sleep(1)
                            print("\n Moriste devorado, a veces los cobardes son los que sobreviven...")
                            next()
                            continue

                        else:
                            print("\n Al quedarte quieto te das cuenta que la criatura no parece querer dañarte.")
                            time.sleep(1) #1
                            print("\n Pasas a lado de la criatura mientras te mira directamente a los ojos.")
                            time.sleep(1) # 0.5
                            print("\n .")
                            time.sleep(1) # 0.5
                            print("\n .")
                            time.sleep(1) # 0.5
                            print("\n .")
                            time.sleep(1) # 1
                            print("\n Al llegar a la habitación te das cuenta de que la puerta fue bloqueada desde dentro...")
                            next()
                            os.system("cls")
                            print("\n Antes de emprender el camino de regreso a la planta baja, encuentras en el suelo otra moneda de hierro.")
                            time.sleep(1)
                            print("\n La moneda tiene la inscripción \"in morte ultima veritas. vicit veritas in omnire\"")
                            line()
                            time.sleep(1)
                            print("\n ¿Tomas la moneda? (S/N)")
                            take_coin_1 = si_no()

                            if take_coin_1 == "s" or take_coin_1 == "S":
                                moneda_morte = True
                                print("Tomaste la moneda")
                            os.system("cls")
                    else:
                        print("\n El sobresalto provoca que sueltes tu fuente de luz.")
                        time.sleep(1)
                        print("\n Al reincorporarte ya no está frente a ti, ahora solo hay frío...")
                        next()
                        time.sleep(1) # 0.5
                        print("\n .")
                        time.sleep(1) # 0.5
                        print("\n .")
                        time.sleep(1) # 0.5
                        print("\n .")
                        time.sleep(1) # 1
                        print("\n Al llegar a la habitación te das cuenta de que la puerta fue bloqueada desde dentro...")
                        next()
                        os.system("cls")
                        print("\n Antes de emprender el camino de regreso a la planta baja, encuentras en el suelo otra moneda de hierro.")
                        time.sleep(1)
                        print("\n La moneda tiene la inscripción \"in morte ultima veritas. vicit veritas in omnire\"")
                        line()
                        time.sleep(1)
                        print("\n ¿Tomas la moneda? (S/N)")
                        take_coin_1 = si_no()

                        if take_coin_1 == "s" or take_coin_1 == "S":
                            moneda_morte = True
                            print("Tomaste la moneda")
                        os.system("cls")
                
                        
                        

        # FINALES

        # Final: Dos monedas y la daga
        if moneda_morte == True and moneda_satana == True and daga == True:
            end()
            time.sleep(1)
            print("\n ¿Entregas dos monedas de hierro o usas la daga? (monedas / daga)")
            while(True):
                try:
                    decision = str(input("(monedas / daga): "))
                    if decision == "Monedas" or decision == "monedas" or decision == "Daga" or decision == "daga":
                        break
                    else:
                        print("Opción inválida, solo se acepta \"monedas\" o \"daga\"")
                        continue
                except:
                    print("Opción inválida, solo se acepta \"monedas\" o \"daga\"")
        
            if decision == "monedas" or decision == "Monedas":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Le entregas ambas monedas... el solamente sonrie mientras pierdes la consciencia...")
                time.sleep(1)
                print("\n Despiertas en la habitación donde inició todo. Es de día y tienes una resaca horrible. Al igual que ese sueño...")
                next()
                time.sleep(1)
                print("\n ###### FELICIDADES! SOBREVIVISTE A LA PESADILLA ######")
                next()
                os.system("cls")
            else:
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Empuñas la daga y apuñalas a \"él\", dos monedas de hierro con la inscripción impía te otorgan el poder para terminar con la amenaza")
                time.sleep(2)
                print("\n Ahora alguien debe tomar su lugar...")
                time.sleep(2) #1
                print("\n Ahora la pesadilla es eterna...")
                next()
                time.sleep(1) #1
                print("\n ###### SOBREVIVISTE A LA PESADILLA, PERO ¿A QUÉ COSTO? ######")
                next()
                os.system("cls")

        # Final: Dos monedas sin daga
        elif moneda_morte == True and moneda_satana == True and daga == False:
            end()
            time.sleep(1) #1
            print("\n ¿Entregas dos monedas de hierro o intentas huir? (monedas / huir)")

            while(True):
                try:
                    decision = str(input("(monedas / huir): "))
            
                    if decision == "Monedas" or decision == "monedas" or decision == "Huir" or decision == "huir":
                        break
            
                    else:
                        print("Opción inválida, solo se acepta \"monedas\" o \"huir\"")
                        continue
            
                except:
                    print("Opción inválida, solo se acepta \"monedas\" o \"huir\"")
        
            if decision == "monedas" or decision == "Monedas":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Le entregas ambas monedas... el solamente sonrie mientras pierdes la consciencia...")
                time.sleep(1)
                print("\n Despiertas en la habitación donde inició todo. Es dedía y tienes una resaca horrible. Al igual que ese sueño...")
                next()
                time.sleep(1)
                print("\n ###### FELICIDADES! SOBREVIVISTE A LA PESADILLA ######")
                next()
                os.system("cls")

            else:
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n ###### NADIE PEUEDE HUIR DE \"ÉL\"... ######")
                time.sleep(1)
                print("\n La muerte es la verdad última. La verdad prevalece sobre todas las cosas.")
                next()
                os.system("cls")

        # Final: Una moneda y daga 1
        elif moneda_morte == False and moneda_satana == True and daga == True:
            end()
            time.sleep(1) #1
            print("\n ¿Entregas una moneda de hierro o usas la daga? (moneda / daga)")

            while(True):
                try:
                    decision = str(input("(moneda / daga): "))

                    if decision == "Moneda" or decision == "moneda" or decision == "Daga" or decision == "daga":
                        break
                    
                    else:
                        print("Opción inválida, solo se acepta \"moneda\" o \"daga\"")
                        continue
                
                except:
                    print("Opción inválida, solo se acepta \"moneda\" o \"daga\"")
        
            if decision == "moneda" or decision == "Moneda":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Entregas una moneda de hierro mientras eres mirado con desdén.")
                time.sleep(1)
                print("\n \"Él\" solo se aleja en la oscuridad.")
                next()
                print("\n ###### NO HAY FIN PARA TU PESADILLA... ######")
                next()
                os.system("cls")

            else:
                os.system("cls")
                scary_face_150()
                next()
                print("\n Apuñalaste a \"Él\" sin tener el poder suficiente.")
                time.sleep(1)
                print("\n ###### EL TORMENTO HA TERMINADO, AL IGUAL QUE TU VIDA ######")
                next()
                os.system("cls")
        
        # Final: Una moneda y daga 2
        elif moneda_morte == True and moneda_satana == False and daga == True:
            end()
            time.sleep(1)
            print("\n ¿Entregas una moneda de hierro o usas la daga? (moneda / daga)")

            while(True):
                try:
                    decision = str(input("(moneda / daga): "))
            
                    if decision == "Moneda" or decision == "moneda" or decision == "Daga" or decision == "daga":
                        break
            
                    else:
                        print("Opción inválida, solo se acepta \"moneda\" o \"daga\"")
                        continue
            
                except:
                    print("Opción inválida, solo se acepta \"moneda\" o \"daga\"")
        
            if decision == "moneda" or decision == "Moneda":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Entregas una moneda de hierro mientras eres mirado con desdén.")
                time.sleep(1)
                print("\n \"Él\" solo se aleja en la oscuridad.")
                time.sleep(1)
                print("\n ###### NO HAY FIN PARA TU PESADILLA... ######")
                next()
                os.system("cls")

            else:
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n Apuñalaste a \"Él\" sin tener el poder suficiente.")
                time.sleep(1)
                print("\n ###### EL TORMENTO HA TERMINADO, AL IGUAL QUE TU VIDA ######")
                next()
                os.system("cls")

        # Final: Una moneda sin daga 1
        elif moneda_morte == False and moneda_satana == True and daga == False:
            end()
            time.sleep(4)
            print("\n ¿Entregas una moneda de hierro o huyes? (moneda / huir)")

            while(True):
                try:
                    decision = str(input("(moneda / huir): "))
            
                    if decision == "Moneda" or decision == "moneda" or decision == "Daga" or decision == "daga":
                        break
            
                    else:
                        print("Opción inválida, solo se acepta \"moneda\" o \"huir\"")
                        continue
            
                except:
                    print("Opción inválida, solo se acepta \"moneda\" o \"huir\"")
        
            if decision == "moneda" or decision == "Moneda":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Entregas una moneda de hierro mientras eres mirado con desdén.")
                time.sleep(1)
                print("\n \"Él\" solo se aleja en la oscuridad.")
                time.sleep(1) #1
                print("\n ###### NO HAY FIN PARA TU PESADILLA... ######")
                next()
                os.system("cls")

            else:
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n ###### NADIE PEUEDE HUIR DE \"ÉL\"... ######")
                time.sleep(1)
                print("\n La muerte es la verdad última. La verdad prevalece sobre todas las cosas.")
                next()
                os.system("cls")

        # Final: Una moneda sin daga 2
        elif moneda_morte == True and moneda_satana == False and daga == False:
            end()
            time.sleep(1) #1
            print("\n ¿Entregas una moneda de hierro o huyes? (moneda / huir)")

            while(True):
                try:
                    decision = str(input("(moneda / huir): "))
            
                    if decision == "Moneda" or decision == "moneda" or decision == "Huir" or decision == "huir":
                        break
            
                    else:
                        print("Opción inválida, solo se acepta \"moneda\" o \"huir\"")
                        continue
            
                except:
                    print("Opción inválida, solo se acepta \"moneda\" o \"huir\"")
        
            if decision == "moneda" or decision == "Moneda":
                os.system("cls")
                line()
                time.sleep(1)
                print("\n Entregas una moneda de hierro mientras eres mirado con desdén.")
                time.sleep(4)
                print("\n \"Él\" solo se aleja en la oscuridad.")
                time.sleep(3)
                print("\n ###### NO HAY FIN PARA TU PESADILLA... ######")
                next()
                os.system("cls")

            else:
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n ###### NADIE PEUEDE HUIR DE \"ÉL\"... ######")
                time.sleep(1)
                print("\n La muerte es la verdad última. La verdad prevalece sobre todas las cosas.")
                next()
                os.system("cls")
        
        # Final: Ninguna moneda con daga
        elif moneda_morte == False and moneda_satana == False and daga == True:
            end()
            time.sleep(1) #1
            print("\n ¿Huyes o usas la daga? (huir / daga)")

            while(True):
                try:
                    decision = str(input("(huir / daga): "))
            
                    if decision == "huir" or decision == "Huir" or decision == "Daga" or decision == "daga":
                        break
            
                    else:
                        print("Opción inválida, solo se acepta \"huir\" o \"daga\"")
                        continue
            
                except:
                    print("Opción inválida, solo se acepta \"huir\" o \"daga\"")
        
            if decision == "huir" or decision == "Huir":
                os.system("cls")
                line()
                scary_face_150()
                next()
                time.sleep(1)
                print("\n ###### NADIE PEUEDE HUIR DE \"ÉL\"... ######")
                time.sleep(1)
                print("\n La muerte es la verdad última. La verdad prevalece sobre todas las cosas.")
                next()
                os.system("cls")

            else:
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n Apuñalaste a \"Él\" sin tener el poder suficiente.")
                time.sleep(1)
                print("\n ###### EL TORMENTO HA TERMINADO, AL IGUAL QUE TU VIDA ######")
                next()
                os.system("cls")
        
        # Final: Ninguna moneda sin daga
        elif moneda_morte == False and moneda_satana == False and daga == False:
            end()
            time.sleep(1) #1
            print("\n ¿Quieres huir? (S/N)")
            scape = si_no()

            if scape == "S" or scape == "s":
                os.system("cls")
                line()
                scary_face_150()
                next()
                print("\n ###### NADIE PEUEDE HUIR DE \"ÉL\"... ######")
                time.sleep(1)
                print("\n La muerte es la verdad última. La verdad prevalece sobre todas las cosas.")
                next()
                os.system("cls")
            
            else:
                os.system("cls")
                line()
                skull_URD()
                next()
                print("\n ###### FELICIDADES, AL MENOS ACEPTASTE TU MUERTE CON DIGNIDAD ######")
                next()
                os.system("cls")

    else:
        print("BIENAVENTURADOS LOS MANSOS, PORQUE SON PRESAS FÁCILES")
        break