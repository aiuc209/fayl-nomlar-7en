import pytest

def get_file_names(file_list):
    return [file.split('.')[0] for file in file_list]

@pytest.mark.parametrize("file_list, expected", [
    (["file1.txt", "file2.pdf", "file3.doc"], ["file1", "file2", "file3"]),
    (["image.jpg", "video.mp4", "audio.wav"], ["image", "video", "audio"]),
    (["document.docx", "presentation.ppt", "spreadsheet.xls"], ["document", "presentation", "spreadsheet"]),
])
def test_get_file_names(file_list, expected):
    assert get_file_names(file_list) == expected
