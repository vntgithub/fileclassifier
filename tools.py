import os
from posixpath import join
import typer
from keras.models import load_model

app = typer.Typer()

def open_db_labels(scenario):
    file = open('/content/drive/MyDrive/Dataset/labels.json',)
    data = json.loads(file.read())
    labels = data[str(scenario)]
    tags = data['tags']
    return labels
    
def get_data_csv_from_result_predict(arr_labels_predicted, arr_labels_name):
    len_data = len(arr_labels_predicted)
    arr_row = []
    for i in range(len(arr_labels_name)):
        total_label = 0
        for label in arr_labels_predicted:
            if label == i:
                total_label += 1
        acc_of_label = total_label/len_data
        arr_row.append([arr_labels_name[i], acc_of_label])
    return arr_row

def make_output_file(output_name_file, arr_row):
    header = ['label','accuracy']
    f = open('result/{}'.format(output_name_file), 'a', encoding='UTF8', newline='')
    writer = csv.writer(f)
    writer.writerow(header)
    for row in arr_row:
        writer.writerow(row)
    f.close()

@app.command()
def file_type_extract(data_dir: str):
    typer.echo(f"Hello {data_dir}")

@app.command()
def analyze_data(
    data_dir: str = typer.Argument(..., help="Data input directory"), 
    block_size: int = typer.Argument(1024, help="For inference, valid block sizes --  512 and 4096 bytes. For training, a positive integer. [default: 4096]"), 
    scenario: int = typer.Argument(1, help="Scenario to assume while classifying. Please refer README for more info. [default: 1]"),
    output_name_file: str = typer.Argument('result.csv',help="Output file name. [default: result.csv]")):
    if scenario < 1 or scenario > 6:
        print('Exception. Scenario: 1-6')
        exit()
    if os.path.isfile('./result/' + output_name_file):
        print('File alredy exist')
        exit()
    
    data_input = open(data_dir, "r")
    model_name = os.path.join('model', '{}_{}.h5'.format(block_size, scenario))
    model = load_model(model_name)
    predict_result = model.predict(data_input)
    arr_labels_predicted = [y.argmax() for y in predict_result]
    arr_labels_name = open_db_labels(scenario)
    arr_row = get_data_csv_from_result_predict(arr_labels_predicted, arr_labels_name)
    make_output_file(arr_row)


if __name__ == "__main__":
    app()