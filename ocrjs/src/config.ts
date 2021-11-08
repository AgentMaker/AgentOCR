const models = {
    'cls': {
        'ch_mul_m_cls':
            'https://bj.bcebos.com/v1/ai-studio-online/1fce1485ebe647c89754fd9f2aeee0a8e815de59b1644875af9013f0b93f56cf?responseContentDisposition=attachment%3B%20filename%3Dch_mul_m_cls.onnx',
    },
    'det': {
        'ch_mul_m_det':
            'https://bj.bcebos.com/v1/ai-studio-online/a0fc871ef7354119a35af83b53fea5dd16826a3e291b4500af8fc1feb0b6b2a6?responseContentDisposition=attachment%3B%20filename%3Dch_mul_m_det.onnx',
        'ch_mul_s_det':
            'https://bj.bcebos.com/v1/ai-studio-online/c905bf277fc44368a2b122b361143cad704d1d4ff5a74a13a9d4c749b02e9d48?responseContentDisposition=attachment%3B%20filename%3Dch_mul_s_det.onnx',
        'en_mul_m_det':
            'https://bj.bcebos.com/v1/ai-studio-online/a85db324f5c54a618712ef670fe6a3a5b4dcf68630744b16a322141c577bf39b?responseContentDisposition=attachment%3B%20filename%3Den_mul_m_det.onnx',
        'ch_mul_v2_c_det':
            'https://bj.bcebos.com/v1/ai-studio-online/485da521bb90456b86469443a4bc6ad25f0e7db1aa624a54b4bc9d2f1dc9db67?responseContentDisposition=attachment%3B%20filename%3Dch_mul_v2_c_det.onnx',
    },
    'rec': {
        'ch_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/78a4d8d082e347798c0b46962c74b7a96aa545c79d2642999aa7a138dc0f3793?responseContentDisposition=attachment%3B%20filename%3Dch_m_rec.onnx',
        'ch_s_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/b8a79b079e084148a1c8fbcbe713496d395ae68efd06419fbfdbf1d1d0046e63?responseContentDisposition=attachment%3B%20filename%3Dch_s_rec.onnx',
        'cht_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/debddf1e4116481196c03e25bb9f8dd37b525adbc9874bd8bb6857d1f4b8ca5b?responseContentDisposition=attachment%3B%20filename%3Dcht_m_rec.onnx',
        'ka_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/a2925709eef94299b1b64e833150c236a81e0b91ded34ab985ff0524030354d9?responseContentDisposition=attachment%3B%20filename%3Dka_m_rec.onnx',
        'te_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/97505fd278cf47e49b04bb1ad3131012e66211948da1432980fbea445ca95ac4?responseContentDisposition=attachment%3B%20filename%3Dte_m_rec.onnx',
        'ta_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/19c24681007e496ba71ed329b7d11628a0660bf05a7b4970a8eb1828f54e6b10?responseContentDisposition=attachment%3B%20filename%3Dta_m_rec.onnx',
        'jp_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/ce668ac53692411fba4762a5c9bd93e930ff7a3557404706ac87bd5730cdbc13?responseContentDisposition=attachment%3B%20filename%3Djp_m_rec.onnx',
        'la_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/a33861210f9c4a21b0cbfcbc5b69da56dec4343734ac484c801886d7574cfa13?responseContentDisposition=attachment%3B%20filename%3Dla_m_rec.onnx',
        'ar_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/3e04471737084487a12bdaab0585f2de25012e9eb5ce4c4b832c83cd15f64377?responseContentDisposition=attachment%3B%20filename%3Dar_m_rec.onnx',
        'kr_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/9dd5aa5dec9e440e81fbead852845d4779655b960ca9433d8d8178cb21066515?responseContentDisposition=attachment%3B%20filename%3Dkr_m_rec.onnx',
        'fr_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/0424f2c98e714e9bb085245b98780ccc8dd059cdf17d45e3aeeb947ed9274176?responseContentDisposition=attachment%3B%20filename%3Dfr_m_rec.onnx',
        'ger_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/219aebb29d4b44d791f4152d97df1a20f3edd69a8ad440bcb596676b63eb4c3a?responseContentDisposition=attachment%3B%20filename%3Dger_m_rec.onnx',
        'cy_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/1ebdfb414e2e4fa2a8a8d7b823b43b3bf2cb5890511440588e20e356414d2de1?responseContentDisposition=attachment%3B%20filename%3Dcy_m_rec.onnx',
        'en_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/68b2ee780b2f4017be955fcb226091e4e557935898004e899614709e9874cc16?responseContentDisposition=attachment%3B%20filename%3Den_m_rec.onnx',
        'de_m_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/d4e698603f6243e98bbf8b7e28585d168e831d6bd852426cb1cbe11a7c487c71?responseContentDisposition=attachment%3B%20filename%3Dde_m_rec.onnx',
        'ch_v2_c_rec':
            'https://bj.bcebos.com/v1/ai-studio-online/365e482fd2f94052924bfe4f5d44aac34866850e00f74625a716fb928da32163?responseContentDisposition=attachment%3B%20filename%3Dch_v2_c_rec.onnx',
    }
}

export { models }