
import { Image , decode } from 'https://deno.land/x/imagescript@v1.2.14/mod.ts'

const { readFile } = Deno;
const { log } = console;


export default async function combine(paths){
    
    const 
        rows = Math.ceil(paths.length / 9) ,
        height = rows * 57 + (rows - 1) * 9 ;


    log('\n',`Using ${ paths.length } emoji ➞ 600 x ${ height }px`,'\n');


    let combined = new Image(600,height);

    let
        x = 0 ,
        y = 0 ;

    for(const path of paths){
        
        const bytes = await readFile(path);
        
        const image = await decode(bytes);

        const
            X = x * (57 + 9) ,
            Y = y * (57 + 9) ;

        combined = combined.composite(image,X,Y); 
        
        x++;
        
        if(x < 9)
            continue;
            
        x = 0;
        y++;
    }
    
    return combined;
}