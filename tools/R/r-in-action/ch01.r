
# Listing 1.1 - A Sample R session
age <- c(1, 3, 5, 2, 11, 9, 3, 9, 12, 3)
weight <- c(4.4, 5.3, 7.2, 5.2, 8.5, 7.3, 6, 10.4, 
                10.2, 6.1)
mean(weight)
sd(weight)
cor(age, weight)
plot(age, weight)

#函数 功能
#help.start() 打开帮助文档首页 
#help("foo")或?foo 查看函数foo的帮助(引号可以省略)
#help.search("foo")或??foo 以foo为关键词搜索本地帮助文档
#example("foo") 函数foo的使用示例(引号可以省略)
#RSiteSearch("foo") 以foo为关键词搜索在线文档和邮件列表存档 
#apropos("foo", mode="function") 列出名称中含有foo的所有可用函数
#data() 列出当前已加载包中所含的所有可用示例数据集
#vignette() 列出当前已安装包中所有可用的vignette文档
#vignette("foo")为主题foo显示指定的vignette文档

      
lmfit <- lm(mpg~wt, data=mtcars)
summary(lmfit)
plot(lmfit)
cook<-cooks.distance(lmfit)
plot(cook)

help.start()
install.packages("vcd")
help(package = "vcd")
library(vcd)
help(Arthritis)
Arthritis
example(Arthritis)
