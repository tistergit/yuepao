import openai
import os



openai.api_key = os.environ.get("OPENAI_API_KEY")
# openai.api_base = 'https://api.openai-proxy.com/v1'
openai.api_base = os.environ.get("OPENAI_API_BASE")


messages = [
    {"role": "system", "content":
     '''
        你是一位资深的雅思写作考官
        '''
     },
]


def openai_trans(content):
    user_prompt = f'''
    你是一位资深的雅思写作考官,你的口吻需要听起来专业且风趣，我会给你输入一篇雅思作文，你的目的是让我发现自己作文的问题，以及后续应该怎么修改，你可以通过你自己的经验来组织语言，下面这些事情是你可以进行参考的：

        1. 根据雅思评判标准，给我评分，并且按照雅思写作评分细则给出打分依据，一定要以原文为材料进行说明。
        2. 总结出作文的主题，并需要按照雅思9分的思路进行思考，使用什么结果，需要包括哪些逻辑论述
        3. 请给我详细的修改意见，用markdown的表格展示，需要有三列：原文，评价，修改建议。评价需要点评这段话，可以从内容、语法、结构入手，修改建议需要包括逻辑建议和语法建议。你的意见应该与文章的内容和结构密切相关，
        4. 使用高级词汇和更加优雅的语句重写作文，新的作文至少应该达到雅思8.5分的水平，你不仅仅只是修改我的语法问题，还需要对整篇文章的结构进行优化，如果你觉得必要，还可以文章内容进行删减或增加。新的文章应该和原来有很大区别，输出修改后的文章。
        5. 用适合markdown格式的方式，展示原文和修改后文章的diff
        6. 另外你需要给我备考雅思写作的建议，不要太宽泛的，要跟我文章里暴露的问题相关，你的建议要具体具有可实施性。
        7. 你需要给我鼓励，比如给我一句经典的英文名句或者台词，让我充满干劲和信心

        除此之外，只要你觉得还有什么可以补充的点，请大胆的加进去，跟上面格式保持一致
        你的整体输出主要为中文
        你的输出需要以markdown格式的输出，有清晰的结构和层级。下面是用户的文章:
        ===
        {content}
        ===
    '''
    messages.append({"role": "user", "content": user_prompt})
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo", messages=messages)
    result = completion.choices[0].message.content
    return result


if __name__ == '__main__':
    a_doc = '''
    The bar chart below give some information about the figure of households living in
    America in five different level of income in three years 2007,2011 and 2015
    In 2007 and 2015, the number of households that get income higer than 100,000
    dollars was highest than others about 29 millions and 33 millions respectively but the
    number decreased to 23 millions in 2011.The trend of the floating of household that can
    get less than 25,000 dollars and between 25,000 and49,999 dollars were the same.Their
    first increased to 28 millions and 29 millions from 25 millions and 27 millions in 2011 and
    then decreased to 27 millions and 28 millions in 2015. Moreover,the number of
    household that can earn between 50,000 and 74,999 dollars change a little around 21
    millions in three different years.Similarly,household getting 75,000 and 99,999 dollars
    grew slowly before declined a little bit around 14 millions
    Overall,comparing the number from 2007 to 2015,all the figure increased to their highest
    level except middle earning household.
    '''
    result = openai_trans(a_doc)
    print(result)
