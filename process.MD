

Oct 10
--

Most of the documentation fields fallback to using the config.py file, so that's the first step:

<img width="626" alt="image" src="https://user-images.githubusercontent.com/99416933/194862056-7b27e45c-52c9-4caf-b625-974ed4b3a6e7.png">


For the Intro video/screenshot , Intro Paragraph and Usage - the config.py file redirects normally to the README:
- Count existent img  tag
- Count existent video tag

<img width="633" alt="image" src="https://user-images.githubusercontent.com/99416933/194862431-91bd3a90-4dcd-49e9-89bd-a21425726435.png">


**Question** - Is the task just checking for the information? Or to add it in the supposed files if not present? Why the question - some of the fields like issue links or source code or authors can be scraped from the GitHub repo

Oct 17
--

Checked information from **config.yml** 

- Summary Sentence
- Source Code link
- Author
- Bug tracker Link
- User Support link

![3](https://user-images.githubusercontent.com/99416933/196192737-b00ce54a-0569-4b10-81d5-a0c1fb31782e.png)


Checked information from **.napari/description.md** 

- Screenshot
- Video
- Usage section
- Intro paragraph

![1](https://user-images.githubusercontent.com/99416933/196192798-c928e32c-ac22-485d-a4fb-c320c3c13832.gif)


Checked information from **npe2 config file** 

- Display Name

![2](https://user-images.githubusercontent.com/99416933/196192829-d15b0f48-29a2-4776-825c-7bbafc2d9ba8.png)


**Otherwise they all fallback to the setup.cfg file 
**


**Created checklist**

An element of the checklist appears as checked if any of its corresponding file locations have the expected metadata (OR statements)


Example 1 (some fields missing)


<img width="446" alt="image" src="https://user-images.githubusercontent.com/99416933/196182974-b62dbba0-f3cd-426d-b09b-bbe83f537d1b.png">


![jhrgiugwr](https://user-images.githubusercontent.com/99416933/196183498-576d7980-a93c-425a-939c-7949bf2eec6b.gif)


Example 2 

By adding a screenshot in the description.md and a CITATION.CFF file

![jiuju](https://user-images.githubusercontent.com/99416933/196184100-4fb63254-4676-4e39-b10c-e72d680f72de.gif)


<img width="459" alt="image" src="https://user-images.githubusercontent.com/99416933/196183978-cfc8dc99-2975-4c24-b965-c5ef3a336efc.png">



**Questions:**

- Should I add the CITATION.CFF to the checklist?
- If there's a metadata field found but in the fallback file, should I suggest the main one? or only if nothing is found?

