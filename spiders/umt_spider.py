import scrapy


class UMTSpider(scrapy.Spider):
    name = "umt_scraper"
    start_urls = [
        'https://www.umt.edu.pk/Academics/Faculty.aspx',
    ]

    def parse(self, response):
        print("hi start")
# response.xpath("//form[@id='aspnetForm']/div[@class='wraper']/div[@class='article']/div[@class='container']/div[@class='row']/div")
        for member in response.css("form#aspnetForm div.wraper div.article div.container div.row div div.staff div.row"):
            image_link = member.css("div.col-lg-2 img.img-responsive::attr(src)").extract_first()
            uni_qualification = member.css("div.col-lg-8 p:nth-child(2)::text").extract_first()
            status = member.css("div.col-lg-8 p:nth-child(3)::text").extract_first()
            email = member.css("div.col-lg-8 p:nth-child(4) a::text").extract_first()
            name = member.css("div.col-lg-8 h4 a::text").extract_first()
            if(name != "None" and image_link != "None" and uni_qualification != "None" and email != "None" and status != "None"):
                yield{
                    'Name': name,
                    'Email': email,
                    'University_Qualification': uni_qualification,
                    'Status': status,
                    'Image_Link': image_link
                }

#response.css("form#aspnetForm div.wraper div.article div.container div.row div div.staff div.row div.col-lg-8 p:nth-child(4) a::text").extract_first()
#response.css("form#aspnetForm div.wraper div.article div.container div.row div div.staff div.row div.col-lg-8 p:nth-child(1)").extract_first()