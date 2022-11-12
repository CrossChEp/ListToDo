def convert_dto_to_dict(dto):
    dto_dict = dict()
    for key, value in dto.dict().items():
        if dto.dict()[key] is None:
            continue
        dto_dict[key] = value
    return dto_dict
