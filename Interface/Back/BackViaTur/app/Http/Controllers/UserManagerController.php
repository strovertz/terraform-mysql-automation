<?php

namespace app\Http\Controllers;
use App\Http\Controllers\Controller;
use App\Models\Supplier;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\DB;

class UserManagerController
{

    public function index(Request $request): JsonResponse
    {

    }

    public function store (Request $request): JsonResponse
    {
            $user = User::query()
                ->$request->all()
                ->save();

            return response()->json(1);
    }


}
