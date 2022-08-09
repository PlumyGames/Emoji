
# Preview Generator

*A **[Deno]** tool to generate previews* <br>
*from this repository's emoticons.*

<br>

## Example Output

![Preview]

<br>
<br>

## Requirements

*To run this tool you just need **[Deno]**.*

<br>
<br>

## Dependencies

*Internal, automatically cached dependencies.*

-   **[ImageScript]**

-   **[Deno STL]**

<br>
<br>

## Running

*Simply call the  `.js`  script as command.*

```Shell
Tools/Preview/.js
```

<br>

*You may have to make it executable.*

```Shell
sudo chmod +x Tools/Preview/.js
```

<br>
<br>

## Basic Design

<br>

1.  Searches for files in the  `/emoji/`  folder.

    <br>

2.  Calculates required height for the preview.

    ```
    Rows = ⌈ EmojiCount ÷ 9 ⌉
    ```
    
    ```
    Height = Rows * 57 + ( Rows - 1 ) * 9
    ```
    
    <br>
    
3.  For every path:

    -   Loads the bytes from the file
    
    -   Decodes the bytes to an image
    
    -   Overlays them onto the preview
    
    <br>
    
4.  Encodes & write the combined image to

    `Resources/Preview.png`

<br>


<!----------------------------------------------------------------------------->

[ImageScript]: https://deno.land/x/imagescript
[Deno STL]: https://deno.land/std
[Deno]: https://deno.land/

[Preview]: ../../Resources/Preview.png