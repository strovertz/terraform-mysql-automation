<?php

namespace App\Http\Controllers;

use App\Models\Itens;
use App\Models\UserModel;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;


class ItensController extends Controller
{
    public function store(Request $request) :JsonResponse
    {
        $id = UserModel::query()
            ->where('email', '=', $request->input('userMail'))
            ->get('id');

        $dataSave = new Itens();
        $dataSave ->id_servico = $request->input('serviceId');
        $dataSave ->id_cliente = $id;
        $dataSave ->save();

        return response()->json($dataSave,200);
    }
}
