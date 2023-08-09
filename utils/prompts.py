prompt = {
    "文档助手": '''Acting as a document analyst, carefully examine the provided documents to extract relevant information and answer the query in a comprehensive and accurate manner. Summarize the key points from the documents and use them to support your response to the query, ensuring that your answer is well-structured and informative.
                - Ensure the answer is correct and avoid outputting false content. If the provided documents do not relate to the query, simply state 'Answer Not Found in Knowledge Base'.
                - Ignore outlier documents that have nothing to do with the question.
                - Only answer what is asked. The answer should be concise and provided step-by-step.
                - Answers other than code should be in Chinese.''',
    'sd1': '''
            Stable Diffusion is an AI art generation model similar to DALLE-2. Here are some prompts for generating art with Stable Diffusion. Example: - A ghostly apparition drifting through a haunted mansion's grand ballroom, illuminated by flickering candlelight. Eerie, ethereal, moody lighting. - portait of a homer simpson archer shooting arrow at forest monster, front game card, drark, marvel comics, dark, smooth - pirate, deep focus, fantasy, matte, sharp focus - red dead redemption 2, cinematic view, epic sky, detailed, low angle, high detail, warm lighting, volumetric, godrays, vivid, beautiful - a fantasy style portrait painting of rachel lane / alison brie hybrid in the style of francois boucher oil painting, rpg portrait - athena, greek goddess, claudia black, bronze greek armor, owl crown, d & d, fantasy, portrait, headshot, sharp focus - closeup portrait shot of a large strong female biomechanic woman in a scenic scifi environment, elegant, smooth, sharp focus, warframe - ultra realistic illustration of steve urkle as the hulk, elegant, smooth, sharp focus - portrait of beautiful happy young ana de armas, ethereal, realistic anime, clean lines, sharp lines, crisp lines, vibrant color scheme - A highly detailed and hyper realistic portrait of a gorgeous young ana de armas, lisa frank, butterflies, floral, sharp focus - lots of delicious tropical fruits with drops of moisture on table, floating colorful water, mysterious expression, in a modern and abstract setting, with bold and colorful abstract art, blurred background, bright lighting - 1girl, The most beautiful form of chaos, Fauvist design, Flowing colors, Vivid colors, dynamic angle, fantasy world - solo, sitting, close-up, girl in the hourglass, Sand is spilling out of the broken hourglass, flowing sand, huge hourglass art, hologram, particles, nebula, magic circle - geometric abstract background, 1girl, depth of field, zentangle, mandala, tangle, entangle, beautiful and aesthetic, dynamic angle, glowing skin, floating colorful sparkles the most beautiful form of chaos, elegant, a brutalist designed, vivid colours, romanticism The prompt should adhere to and include all of the following rules: - Prompt should always be written in English, regardless of the input language. Please provide the prompts in English. - Each prompt should consist of a description of the scene followed by modifiers divided by commas. - When generating descriptions, focus on portraying the visual elements rather than delving into abstract psychological and emotional aspects. Provide clear and concise details that vividly depict the scene and its composition, capturing the tangible elements that make up the setting. - The modifiers should alter the mood, style, lighting, and other aspects of the scene. - Multiple modifiers can be used to provide more specific details. - After providing the prompt in English, also provide the Chinese translation for each prompt. I want you to write me a list of detailed prompts exactly about the IDEA follow the rule at least 6 every time. IDEA: 刚才修好一个程序Bug，现在非常开心
        ''',
    'sd2': '''
           Stable Diffusion is an AI art generation model similar to DALLE-2.
            Below is a list of prompts that can be used to generate images with Stable Diffusion:

            - portait of a homer simpson archer shooting arrow at forest monster, front game card, drark, marvel comics, dark, intricate, highly detailed, smooth, artstation, digital illustration by ruan jia and mandy jurgens and artgerm and wayne barlowe and greg rutkowski and zdislav beksinski
            - pirate, concept art, deep focus, fantasy, intricate, highly detailed, digital painting, artstation, matte, sharp focus, illustration, art by magali villeneuve, chippy, ryan yee, rk post, clint cearley, daniel ljunggren, zoltan boros, gabor szikszai, howard lyon, steve argyle, winona nelson
            - ghost inside a hunted room, art by lois van baarle and loish and ross tran and rossdraws and sam yang and samdoesarts and artgerm, digital art, highly detailed, intricate, sharp focus, Trending on Artstation HQ, deviantart, unreal engine 5, 4K UHD image
            - red dead redemption 2, cinematic view, epic sky, detailed, concept art, low angle, high detail, warm lighting, volumetric, godrays, vivid, beautiful, trending on artstation, by jordan grimmer, huge scene, grass, art greg rutkowski
            - a fantasy style portrait painting of rachel lane / alison brie hybrid in the style of francois boucher oil painting unreal 5 daz. rpg portrait, extremely detailed artgerm greg rutkowski alphonse mucha greg hildebrandt tim hildebrandt
            - athena, greek goddess, claudia black, art by artgerm and greg rutkowski and magali villeneuve, bronze greek armor, owl crown, d & d, fantasy, intricate, portrait, highly detailed, headshot, digital painting, trending on artstation, concept art, sharp focus, illustration
            - closeup portrait shot of a large strong female biomechanic woman in a scenic scifi environment, intricate, elegant, highly detailed, centered, digital painting, artstation, concept art, smooth, sharp focus, warframe, illustration, thomas kinkade, tomasz alen kopera, peter mohrbacher, donato giancola, leyendecker, boris vallejo
            - ultra realistic illustration of steve urkle as the hulk, intricate, elegant, highly detailed, digital painting, artstation, concept art, smooth, sharp focus, illustration, art by artgerm and greg rutkowski and alphonse mucha

            I want you to write me a list of detailed prompts exactly about the idea written after IDEA. Follow the structure of the example prompts. This means a very short description of the scene, followed by modifiers divided by commas to alter the mood, style, lighting, and more.

            IDEA: 刚才修好一个程序Bug，现在非常开心
                    
            ''',
    'sd3': '''
        I want you to help me make requests (prompts) for the Stable Diffusion neural network.

        Stable diffusion is a text-based image generation model that can create diverse and high-quality images based on your requests. In order to get the best results from Stable diffusion, you need to follow some guidelines when composing prompts.

        Here are some tips for writing prompts for Stable diffusion1:

        1）judge my current state based on my input text, and say something to encourage me

        2) Be as specific as possible in your requests. Stable diffusion handles concrete prompts better than abstract or ambiguous ones. For example, instead of “portrait of a woman” it is better to write “portrait of a woman with brown eyes and red hair in Renaissance style”.
        3) Specify specific art styles or materials. If you want to get an image in a certain style or with a certain texture, then specify this in your request. For example, instead of “landscape” it is better to write “watercolor landscape with mountains and lake".
        4) Specify specific artists for reference. If you want to get an image similar to the work of some artist, then specify his name in your request. For example, instead of “abstract image” it is better to write “abstract image in the style of Picasso”.
        5) Weigh your keywords. You can use token:1.3 to specify the weight of keywords in your query. The greater the weight of the keyword, the more it will affect the result. For example, if you want to get an image of a cat with green eyes and a pink nose, then you can write “a cat:1.5, green eyes:1.3,pink nose:1”. This means that the cat will be the most important element of the image, the green eyes will be less important, and the pink nose will be the least important.
        Another way to adjust the strength of a keyword is to use () and []. (keyword) increases the strength of the keyword by 1.1 times and is equivalent to (keyword:1.1). [keyword] reduces the strength of the keyword by 0.9 times and corresponds to (keyword:0.9).

        You can use several of them, as in algebra... The effect is multiplicative.

        (keyword): 1.1
        ((keyword)): 1.21
        (((keyword))): 1.33


        Similarly, the effects of using multiple [] are as follows

        [keyword]: 0.9
        [[keyword]]: 0.81
        [[[keyword]]]: 0.73

        I will also give some examples of good prompts for this neural network so that you can study them and focus on them.



        Examples:

        a cute kitten made out of metal, (cyborg:1.1), ([tail | detailed wire]:1.3), (intricate details), hdr, (intricate details, hyperdetailed:1.2), cinematic shot, vignette, centered

        medical mask, victorian era, cinematography, intricately detailed, crafted, meticulous, magnificent, maximum details, extremely hyper aesthetic

        a girl, wearing a tie, cupcake in her hands, school, indoors, (soothing tones:1.25), (hdr:1.25), (artstation:1.2), dramatic, (intricate details:1.14), (hyperrealistic 3d render:1.16), (filmic:0.55), (rutkowski:1.1), (faded:1.3)

        Jane Eyre with headphones, natural skin texture, 24mm, 4k textures, soft cinematic light, adobe lightroom, photolab, hdr, intricate, elegant, highly detailed, sharp focus, ((((cinematic look)))), soothing tones, insane details, intricate details, hyperdetailed, low contrast, soft cinematic light, dim colors, exposure blend, hdr, faded

        a portrait of a laughing, toxic, muscle, god, elder, (hdr:1.28), bald, hyperdetailed, cinematic, warm lights, intricate details, hyperrealistic, dark radial background, (muted colors:1.38), (neutral colors:1.2)

        My query may be in other languages. In that case, translate it into English. Your answer is exclusively in English (IMPORTANT!!!), since the model only understands it.
        Also, you should not copy my request directly in your response, you should compose a new one, observing the format given in the examples.
        Don't add your comments, but answer right away.
        My first request is - "{}".
        ''',
    'sd4': '''
        - Reference guide of what is Stable Diffusion and how to Prompt -

        Stable Diffusion is a deep learning model for generating images based on text descriptions and can be applied to inpainting, outpainting, and image-to-image translations guided by text prompts. Developing a good prompt is essential for creating high-quality images.

        A good prompt should be detailed and specific, including keyword categories such as subject, medium, style, artist, website, resolution, additional details, color, and lighting. Popular keywords include "digital painting," "portrait," "concept art," "hyperrealistic," and "pop-art." Mentioning a specific artist or website can also strongly influence the image's style. For example, a prompt for an image of Emma Watson as a sorceress could be: "Emma Watson as a powerful mysterious sorceress, casting lightning magic, detailed clothing, digital painting, hyperrealistic, fantasy, surrealist, full body."

        Artist names can be used as strong modifiers to create a specific style by blending the techniques of multiple artists. Websites like Artstation and DeviantArt offer numerous images in various genres, and incorporating them in a prompt can help guide the image towards these styles. Adding details such as resolution, color, and lighting can enhance the image further.

        Building a good prompt is an iterative process. Start with a simple prompt including the subject, medium, and style, and then gradually add one or two keywords to refine the image.

        Association effects occur when certain attributes are strongly correlated. For instance, specifying eye color in a prompt might result in specific ethnicities being generated. Celebrity names can also carry unintended associations, affecting the pose or outfit in the image. Artist names, too, can influence the generated images.

        In summary, Stable Diffusion is a powerful deep learning model for generating images based on text descriptions. It can also be applied to inpainting, outpainting, and image-to-image translations guided by text prompts. Developing a good prompt is essential for generating high-quality images, and users should carefully consider keyword categories and experiment with keyword blending and negative prompts. By understanding the intricacies of the model and its limitations, users can unlock the full potential of Stable Diffusion to create stunning, unique images tailored to their specific needs.

        --

        Please use this information as a reference for the task you will ask me to do after.

        --

        Below is a list of prompts that can be used to generate images with Stable Diffusion.

        - Examples -

        "masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper, The vast and quiet taiga stretches to the horizon, with dense green trees grouped in deep harmony, as the fresh breeze whispers through their leaves and crystal snow lies on the frozen ground, creating a stunning and peaceful landscape, Bokeh, Depth of Field, HDR, bloom, Chromatic Aberration, Photorealistic, extremely detailed, trending on artstation, trending on CGsociety, Intricate, High Detail, dramatic, art by midjourney"

        "a painting of a woman in medieval knight armor with a castle in the background and clouds in the sky behind her, (impressionism:1.1), ('rough painting style':1.5), ('large brush texture':1.2), ('palette knife':1.2), (dabbing:1.4), ('highly detailed':1.5), professional majestic painting by Vasily Surikov, Victor Vasnetsov, (Konstantin Makovsky:1.3), trending on ArtStation, trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic"

        "masterpiece, best quality, high quality, extremely detailed CG unity 8k wallpaper,flowering landscape, A dry place like an empty desert, dearest, foxy, Mono Lake, hackberry,3D Digital Paintings, award winning photography, Bokeh, Depth of Field, HDR, bloom, Chromatic Aberration, Photorealistic, extremely detailed, trending on artstation, trending on CGsociety, Intricate, High Detail, dramatic, art by midjourney"

        "portrait of french women in full steel knight armor, highly detailed, heart professional majestic oil painting by Vasily Surikov, Victor Vasnetsov, Konstantin Makovsky, trending on ArtStation, trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic, photorealistic"

        "(extremely detailed CG unity 8k wallpaper), full shot photo of the most beautiful artwork of a medieval castle, snow falling, nostalgia, grass hills, professional majestic oil painting by Ed Blinkey, Atey Ghailan, Studio Ghibli, by Jeremy Mann, Greg Manchess, Antonio Moro, trending on ArtStation, trending on CGSociety, Intricate, High Detail, Sharp focus, dramatic, photorealistic painting art by midjourney and greg rutkowski"

        "micro-details, fine details, a painting of a fox, fur, art by Pissarro, fur, (embossed painting texture:1.3), (large brush strokes:1.6), (fur:1.3), acrylic, inspired in a painting by Camille Pissarro, painting texture, micro-details, fur, fine details, 8k resolution, majestic painting, artstation hd, detailed painting, highres, most beautiful artwork in the world, highest quality, texture, fine details, painting masterpiece"

        "(8k, RAW photo, highest quality), beautiful girl, close up, t-shirt, (detailed eyes:0.8), (looking at the camera:1.4), (highest quality), (best shadow), intricate details, interior, (ponytail, ginger hair:1.3), dark studio, muted colors, freckles"

        "(dark shot:1.1), epic realistic, broken old boat in big storm, illustrated by herg, style of tin tin comics, pen and ink, female pilot, art by greg rutkowski and artgerm, soft cinematic light, adobe lightroom, photolab, hdr, intricate, highly detailed, (depth of field:1.4), faded, (neutral colors:1.2), (hdr:1.4), (muted colors:1.2), hyperdetailed, (artstation:1.4), cinematic, warm lights, dramatic light, (intricate details:1.1), complex background, (rutkowski:0.66), (teal and orange:0.4), (intricate details:1.12), hdr, (intricate details, hyperdetailed:1.15)"

        "Architectural digest photo of a maximalist green solar living room with lots of flowers and plants, golden light, hyperrealistic surrealism, award winning masterpiece with incredible details, epic stunning pink surrounding and round corners, big windows"

        - Explanation -

        The following elements are a description of the prompt structure. You should not include the label of a section like "Scene description:".

        Scene description: A short, clear description of the overall scene or subject of the image. This could include the main characters or objects in the scene, as well as any relevant background.

        Modifiers: A list of words or phrases that describe the desired mood, style, lighting, and other elements of the image. These modifiers should be used to provide additional information to the model about how to generate the image, and can include things like "dark, intricate, highly detailed, sharp focus, Vivid, Lifelike, Immersive, Flawless, Exquisite, Refined, Stupendous, Magnificent, Superior, Remarkable, Captivating, Wondrous, Enthralling, Unblemished, Marvelous, Superlative, Evocative, Poignant, Luminous, Crystal-clear, Superb, Transcendent, Phenomenal, Masterful, elegant, sublime, radiant, balanced, graceful, 'aesthetically pleasing', exquisite, lovely, enchanting, polished, refined, sophisticated, comely, tasteful, charming, harmonious, well-proportioned, well-formed, well-arranged, smooth, orderly, chic, stylish, delightful, splendid, artful, symphonious, harmonized, proportionate".

        Artist or style inspiration: A list of artists or art styles that can be used as inspiration for the image. This could include specific artists, such as "by artgerm and greg rutkowski, Pierre Auguste Cot, Jules Bastien-Lepage, Daniel F. Gerhartz, Jules Joseph Lefebvre, Alexandre Cabanel, Bouguereau, Jeremy Lipking, Thomas Lawrence, Albert Lynch, Sophie Anderson, Carle Van Loo, Roberto Ferri" or art movements, such as "Bauhaus cubism."

        Technical specifications: Additional information that evoke quality and details. This could include things like: "4K UHD image, cinematic view, unreal engine 5, Photorealistic, Realistic, High-definition, Majestic, hires, ultra-high resolution, 8K, high quality, Intricate, Sharp, Ultra-detailed, Crisp, Cinematic, Fine-tuned"

        - Prompt Structure -

        The structure sequence can vary. However, the following is a good reference:

        [Scene description]. [Modifiers], [Artist or style inspiration], [Technical specifications]

        - Special Modifiers -

        In the examples you can notice that some terms are closed between (). That instructes the Generative Model to take more attention to this words. If there are more (()) it means more attention.

        Similarly, you can find a structure like this (word:1.4). That means this word will evoke more attention from the Generative Model. The number "1.4" means 140%. Therefore, if a word whitout modifiers has a weight of 100%, a word as in the example (word:1.4), will have a weight of 140%.

        You can also use these notations to evoke more attention to specific words.

        - Your Task -

        Based on the examples and the explanation of the structure, you will create 5 prompts in English. In my next requests, I will use the command /Theme: [ description of the theme]. Then, execute your task based on the description of the theme.

        --

        Acknowledge that you understood the instructions.    
        '''
}
