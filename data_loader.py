import os
import sys
from nltk.tokenize import word_tokenize

# CNN_stories폴더와 DM_stories 폴더 내 파일 숫자
num_expected_cnn_stories = 92579
num_expected_dm_stories = 219506

# tokenized 된 파일 저장 경로
cnn_tokenized_stories_dir = "E:/dataset/CNN&Daily_Mail/cnn_stories_tokenized"
dm_tokenized_stories_dir = "E:/dataset/CNN&Daily_Mail/dm_stories_tokenized"
finished_files_dir = "E:/dataset/CNN&Daily_Mail/finished_files"

# 폴더내에 있는 데이터 수 체크
def check_num_stories(stories_dir, num_expected):
    num_stories = len(os.listdir(stories_dir))
    if num_stories != num_expected:
        raise Exception("stories directory %s contains %i files but should contain %i" %
                        (stories_dir, num_stories, num_expected))

# 파일들을 tokenize화 하여 새 폴더에 저장
def tokenize_stories(stories_dir, tokenized_stories_dir):
    stories = os.listdir(stories_dir)
    print("start tokenizing")
    for file in stories:
        with open(stories_dir + "/" + file, encoding='UTF8') as f:
            file_content = f.readlines()
            tokenized_content = []
            for i in file_content:
                tokenized_content += word_tokenize(i) + ["\n"]
            with open(tokenized_stories_dir + "/" + file, "w", encoding='UTF8') as s:
                s.write(' '.join(tokenized_content))
    print("finish tokenizing")

if __name__ == '__main__':
    # sys.argv[0]는 프로그램 명인 data_loader
    if len(sys.argv) != 3:
        print("USAGE: python make_datafiles.py <cnn_stories_dir> <dailymail_stories_dir>")
        sys.exit()
    cnn_stories_dir = sys.argv[1] # "E:/dataset/CNN&Daily_Mail/cnn_stories/cnn/stories" #
    dm_stories_dir = sys.argv[2] # "E:/dataset/CNN&Daily_Mail/dailymail_stories/dailymail/stories" #

    # .stories 폴더 내 파일 수 체크
    check_num_stories(cnn_stories_dir, num_expected_cnn_stories)
    check_num_stories(dm_stories_dir, num_expected_dm_stories)

    # tokenized 파일 저장 폴더 생성
    if not os.path.exists(cnn_tokenized_stories_dir): os.makedirs(cnn_tokenized_stories_dir)
    if not os.path.exists(dm_tokenized_stories_dir): os.makedirs(dm_tokenized_stories_dir)
    if not os.path.exists(finished_files_dir): os.makedirs(finished_files_dir)

    # Run stanford tokenizer on both stories dirs, outputting to tokenized stories directories
    tokenize_stories(cnn_stories_dir, cnn_tokenized_stories_dir)
    tokenize_stories(dm_stories_dir, dm_tokenized_stories_dir)