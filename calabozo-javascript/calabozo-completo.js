// Buscar como importar time, random, os (random solucionado)

const { chown } = require("fs");
const { callbackify } = require("util");

// --------------- DRAW FUNCTIONS ---------------

const line = () => {
    console.log("-----------------------------------------------------------------------------------------");
};


const skull_URD = () => {
    console.log(`\n
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
    `);
};


const creature = () => {
    console.log(`\n
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
        `
    );
};


const kit_face = () => {
    (`\n                                                                                
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
                                                                                                    
  `);
};


const scary_face = () => {
    console.log(`\n
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
                                     .                       .,:..                                     `
    );
};


const face_hands = () => {
    console.log(`\n
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
                                                                           ..            ...........                                           ..`
    );
};


const big_mouth = () => {
    console.log(`\n
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
 .'.         .'.                    .''.                  .'''..       ..''''''.'''''... ..'.       `

    );
};


const face_flesh = () => {
    console.log(`\n
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
...                                                                                                                                   ..           ...`

    );
};


// --------------- LOGIC FUNCTIONS ---------------

// Solucion 1 (mal) -----------------------------------------------------------------
// let option = (option1, option2, callback) => {
//     const readline = require("readline");
//     let read = readline.createInterface( {
//         input : process.stdin,
//         output : process.stdout
//     });

//     read.question(`${option1}/${option2}: `, (choice) => {
//         const allowedValues = [option1, option2];
//         if (allowedValues.includes(choice)) { // solo si coincide con la lista de opciones disponibles, recibidas por la función que invoca, puede continuar
//             console.log("ok!");
//             read.close();
//         } else {
//             console.log(`Opcion inválida, intentalo de nuevo!!`);
//             read.close(); // Se cierra la interfaz antes de llamar de nuevo a la función, para no acumular argumentos
//             option(option1, option2, callback); // Llamar recursivamente a la función con los mismos argumentos y callback
//         };
//         callback(choice)
//     });
// };


// let yes_no = () => {
//     let option1 = "yes";
//     let option2 = "no";
    
// }

// yes_no()



// Solucion 2 ------------------------------------------------------------------

let option = (callback) => {
    const readline = require("readline");
    let read = readline.createInterface( {
        input : process.stdin,
        output : process.stdout
    });

    read.question(`¿Qué eliges?: `, (choice) => {
        read.close();
        callback(choice);
    });
};

function yes_no(callback) {
    option ( (choice) => {
        let allowedValues = ["Yes", "yes", "No", "no"];
        try {
            if (allowedValues.includes(choice)){
                callback(choice);
            } else {
                console.log(`Opción inválida, inténtalo de nuevo!!`);
                yes_no(callback);
            }
        } catch (error) {
            if (error instanceof TypeError) {
                console.error(`Se produjo un error del tipo: `, error.message);
                yes_no(callback);
            } else {
                console.log(`Opción inválida, inténtalo de nuevo!!`);
                yes_no(callback);
            }
        };
    });
};


yes_no ((choice) => {
    if (choice == "No" || choice == "no") {
        console.log("En efecto, no.");
    } else if (choice == "Yes" || choice == "yes"){
        console.log("En efecto, si.");
    } else {
        console.log("Pero que ha pasao?!");
    }
});