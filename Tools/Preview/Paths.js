
import { fromFileUrl , dirname , join } from 'https://deno.land/std@0.151.0/path/mod.ts'


const 
    folder = dirname(fromFileUrl(import.meta.url)) ,
    root = join(folder,'..','..') ;
    
    
export const output = join(root,'Resources','Preview.png');
export const emojis = join(root,'emoji');

