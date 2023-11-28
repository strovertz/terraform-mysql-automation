<?php

namespace App\Http\Controllers;

use App\Models\UserModel;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;

class UserManagerController extends Controller
{
    public function index(Request $request): JsonResponse
    {
        $email = $request->input('email');
        $password = $request->input('password');

        $user = UserModel::query()
            ->where('email',  $email)
            ->where('senha' , $password)
            ->firstOrFail();

        return response()->json(`data : ${user}`, 200);
    }

    public function store (Request $request): JsonResponse
    {
        $user = new UserModel();
        $user->nome = $request->input('nameUser');
        $user->senha = $request->input('password');
        $user->email = $request->input('email');
        $user->telefone = $request->input('phone');
        $user->genero = $request->input('GenderSelectedOption');
        $user->endereco = $request->input('addressUser');
        $user->cpf = $request->input('cpf');
        $user->data_nasc = \Carbon\Carbon::parse($request->input('birthday'))->format('Y/m/d');
        $user->save();

        return response()->json(['data_updated' => $request->all()], 200);
    }


}
