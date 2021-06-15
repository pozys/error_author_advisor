import conf_storage_history_handler as history_handler

def get_metadata_from_raw_data(raw_data: list):
    df_report = history_handler.df_raw_report()
    df_report = df_report[['changed_data']].drop_duplicates().reset_index(drop=True)

    metadata = []

    if df_report.size == 0:
        return metadata

    df_report['metadata_array'] = df_report['changed_data']. \
        apply(lambda item : str_to_set_with_index(item))
    
    for item in raw_data:
        item_array = str_to_set_with_index(item)

        df_report['result'] = df_report['metadata_array']. \
            map(lambda metadata : len(item_array.intersection(metadata)) == len(metadata))
        result = df_report[df_report['result']].reset_index(drop=True)

        if result.size == 0:
            continue

        metadata.append(result['changed_data'].max())     

    return set(metadata)

def str_to_set_with_index(item: str):
    return set(str(i) + '_' + x for i, x in enumerate(item.split('.')))
