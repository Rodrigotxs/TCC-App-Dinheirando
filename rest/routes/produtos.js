const express = require('express');
const router = express.Router();

// Retorna todos os produtos
router.get('/', (req,res,next) => {
    res.status(200).send({
        mensagem: 'Usando o GET dentro da rota de produto'
    });
});

// Insere um produto
router.post('/',(req,res,next) => {

    const produto = {
        nome: req.body.nome,
        preco: req.body.preco
    }

    res.status(201).send({
        mensagem: 'Insere um produto',
        produtoCriado: produto
    });
});

// Retorna os dados de um produto
router.get('/:id_produto', (req,res,next) => {
    const id = req.params.id_produto;

    if(id === 'especial'){
        res.status(200).send({
            mensagem: 'Vc descobriu o ID especial',
            id: id
        });
    }else{
        res.status(200).send({
            mensagem: 'Vc passou um ID'
        })
    }

});

//Altera um produto
router.patch('/',(req,res,next) => {
    res.status(201).send({
        mensagem: 'Usando o PATCH dentro da rota de produtos'
    });
});

//Exclui um produto
router.delete('/',(req,res,next) => {
    res.status(201).send({
        mensagem: 'Usando o DELETE dentro da rota de produtos'
    });
});


module.exports = router;